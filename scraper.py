import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


token = 'seu_token'
chat_id = "seu_chat_id"
df = pd.DataFrame(columns=["Data e hora","Valor"])


def mensage_telegram(token,chat_id,mensagem):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': mensagem}
    response = requests.post(url, data=data)
    return response
  
# Usando nesse codigo um site para scrappar o valor da racao do meu pet              
link = "https://www.americanpet.com.br/7898604432968-racao-seca-nd-prime-canine-adultos-maxi-cordeiro-10-1kg/p"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}


while True:
    try:
        
        print("Acessando a página...")
        rqst = requests.get(link, headers=headers)
        rqst.raise_for_status() # Retorna um erro se houver um problema de requisiçao
        print("Página acessada")
        
        site = BeautifulSoup(rqst.text, "html.parser")
        
        # Captura valor do produto        
        site_valor = site.find("p", class_="amepettatix-store-5-x-priceSubscription--withDiscount")
        
        if site_valor:
            data_hora = datetime.now(tz=None).strftime("%x %H:%M:%S")
            print(f"Valor do produto em {data_hora} -- {site_valor.text}")
            
            nova_linha= {"Data e hora":data_hora,"Valor": site_valor.text}
            nova_linha_df= pd.DataFrame([nova_linha])
            df = pd.concat([df, nova_linha_df], ignore_index=True)
            
            df.to_csv(r"C:\Users\handr\Documents\daily_valor_racao.csv", index=False)
            
            # Salvar um arqv CSV
            # O codigo nao estava executando via cmd, pois o arqv csv nao erra acessivel pelo cmd
            # Ao salver usando um caminho absoluto. Independente de onde estiver sendo executado pelo cmd 
            df.to_csv(r"C:\Users\handr\Documents\daily_valor_racao.csv", index=False)

            # Envia mensagem para o Telegram
            mensagem = f"Valor da ração em {data_hora} é {site_valor.text}"
            mensage_telegram(token, chat_id, mensagem)
            
            
        else:
            print("Não foi possível encontrar o valor do produto.")

    # Caso ocorra um erro de solicitaçao HTTP.
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")  
    except Exception as e:
        print(f"Ocorreu um erro {e}")
    finally:
        print("Esperando 6 horas para a próxima verificação")
        time.sleep(21600)