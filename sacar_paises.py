from bs4 import BeautifulSoup
import requests

url='https://www.nationsonline.org/oneworld/countrynames_spanish.htm'
doc = requests.get(url)
soup = BeautifulSoup(doc.text, 'html.parser')
paises = []
def parse_txt(txt, mode=0):
    if mode==0:
        result=''
        sin_esp=txt.split(' ')
        for p in sin_esp:
            result+=p
        sin_saltos=result.split('\n')
        result=''
        for p in sin_saltos:
            result+=p
        return result
    else:
        sin_saltos=txt.split('\n')
        result=''
        for p in sin_saltos:
            result+=p
        return result


try:
    tables=soup.find_all('table')
    for t_body in tables:
        for child in t_body.find_all('a'):
            print(child.string)
            paises.append(child.string)
    with open('listado_paises.txt', 'w+') as file:
        for line in paises:
            file.write(line)
            file.write('\n')    
    with open('codigo_paises.txt', 'w+') as file:
        for line in paises:
            sin_esp=parse_txt(line, mode=0)
            pais=parse_txt(line, mode=1)
            code_line="<option value='{}'>{}</option>".format(sin_esp, pais)
            file.write(code_line)
            file.write('\n')
        
        
except Exception as e:
    print(e)

