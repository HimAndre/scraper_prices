import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


df = pd.DataFrame(columns=["Data e hora", "Moeda", "Valor"])

                  
link = "https://finance.yahoo.com/quote/USDBRL=X/?guccounter=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}

while True:
    try:
        
        rqst = requests.get(link, headers=headers)
        site = BeautifulSoup(rqst.text, "html.parser")
 
        site_valor = site.find("fin-streamer", class_="livePrice yf-1tejb6")
        
        if site_valor:
            data_hora = datetime.now(tz=None).strftime("%x %H:%M:%S")
            print(f"Dollar price in {data_hora} -- {site_valor.text}")
            
            nova_linha= {"Data e hora":data_hora, "Moeda": "Dolar","Valor": site_valor.text}
            nova_linha_df= pd.DataFrame([nova_linha])
            df = pd.concat([df, nova_linha_df], ignore_index=True)

            data_csv = df.to_csv("daily_dollar.csv", index=False)
        
        else:
            print("Não foi possível encontrar o valor do dólar.")

    except KeyboardInterrupt:
        print("Coleta interrompida pelo usuário")

    
    time.sleep(600)