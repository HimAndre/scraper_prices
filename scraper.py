import requests
from bs4 import BeautifulSoup

link = "https://finance.yahoo.com/quote/USDBRL=X/?guccounter=1"
headers = {
  "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}
  
rqst = requests.get(link, headers=headers)

site = BeautifulSoup(rqst.text, "html.parser")

site_valor = site.find("fin-streamer", class_= "livePrice yf-1i5aalm")
if site_valor:
  print(f"Valor do dolar: {site_valor.text}")
else:
  print("Não foi possível encontrar o valor.")

