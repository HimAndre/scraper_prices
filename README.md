Dólar Scraper

É um projeto simples de web scraping para coletar o valor atual do dólar de um site de câmbio e exibi-lo ou armazená-lo para futuras consultas.

Funcionalidades
Coleta o valor atual do dólar em tempo real de uma fonte online.
Armazena os dados em um arquivo CSV ou banco de dados (SQLite, por exemplo).
Pode ser configurado para realizar a coleta em intervalos regulares de tempo.

Requisitos:
Para executar este scraper, você precisa ter as seguintes libs:

requests
beautifulsoup4
pandas (opcional, para armazenar em DataFrames)
sqlite3 (opcional, para uso com banco de dados SQLite)

Executar o script

O script principal para coletar os dados está localizado no arquivo scraper.py.

Personalização:

URL da fonte: A URL do site de onde o valor do dólar será coletado pode ser ajustada diretamente no código, na variável url.
Armazenamento dos dados: Os dados coletados podem ser salvos em um arquivo CSV ou diretamente em um banco de dados. 
