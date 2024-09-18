import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" }

requesicao = requests.get(link, headers=headers)
# print(requesicao)
# print(requesicao.text)

site = BeautifulSoup(requesicao.text, "html.parser")
# print(site.prettify())

# titulo = site.find("title")
# print(titulo)

# pesquisa = site.find_all("textarea")
# print(pesquisa)

# pesquisa2 = site.find("textarea, class_=gLFyf")
# print(pesquisa2)
# print(pesquisa2["value"])

cotacao_dolar = site.find("span", class_="SwHCTb" )
print(cotacao_dolar)
print(cotacao_dolar["data-value"])
#print(cotacao_dolar.get_text())
