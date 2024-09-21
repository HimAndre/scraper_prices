import time
import pandas as pd
from scraper import site_valor
from datetime import datetime

df = pd.DataFrame(columns=["Data e hora", "Moeda", "Valor"])

intervalo_tempo = 600

try:
  while True:
    get_dollar = site_valor
    
    if get_dollar:
      
      data_hora = datetime.now(tz=None).strftime("%Y-%m-%d %H:%M:%S")
      
      nova_linha= {"Data e hora": data_hora, "Moeda": "Dólar", "Valor": get_dollar}
      df = pd.concat([df, pd.DataFrame([nova_linha])])

      print(df)
    
    else:
      print("Não foi possivel obter o valor do dólar")
      
    time.sleep(intervalo_tempo)

except KeyboardInterrupt:
  print("Coleta interrompida pelo usuário")
  