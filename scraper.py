import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


token = ''
chat_id = ""
df = pd.DataFrame(columns=["Data e hora","Valor"])


def mensage_telegram(token,chat_id,mensagem):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': mensagem}
    response = requests.post(url, data=data)
    return response
  
               
link = "https://www.americanpet.com.br/7898604432968-racao-seca-nd-prime-canine-adultos-maxi-cordeiro-10-1kg/p"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}


while True:
    try:
        
        rqst = requests.get(link, headers=headers)
        site = BeautifulSoup(rqst.text, "html.parser")
                
        site_valor = site.find("p", class_="amepettatix-store-5-x-priceSubscription--withDiscount")
        if site_valor:
            data_hora = datetime.now(tz=None).strftime("%x %H:%M:%S")
            print(f"Dollar price in {data_hora} -- {site_valor.text}")
            
            nova_linha= {"Data e hora":data_hora,"Valor": site_valor.text}
            nova_linha_df= pd.DataFrame([nova_linha])
            df = pd.concat([df, nova_linha_df], ignore_index=True)
            data_csv = df.to_csv("daily_valor_racao.csv", index=False)

            mensagem = f"Valor da ração em {data_hora} é {site_valor.text}"
            mensage_telegram(token, chat_id, mensagem)
            
            
        else:
            print("Não foi possível encontrar o valor do produto.")

    except KeyboardInterrupt:
        print("Coleta interrompida pelo usuário")

    
    time.sleep(21600)