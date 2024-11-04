Dólar Scraper

É um projeto simples de web scraping para coletar dados/armazenamento.

Funcionalidades

Coleta o valor atual do valor em tempo real de uma fonte online (valor de moeda, produto e afins)
Armazena os dados em um arquivo CSV ou banco de dados (SQLite, por exemplo).
Pode ser configurado para realizar a coleta em intervalos regulares de tempo.

Eu defini um produto que eu gostaria de verificar o preco constantemente e assim possibilitar a compra no momento mais oportuno.

Requisitos:
Para executar este scraper, você precisa ter as seguintes libs:

requests
beautifulsoup4
pandas (opcional, para armazenar em DataFrames)
sqlite3 (opcional, para uso com banco de dados SQLite)

Entendendo que a alguns sites alteram os valores da classes que tornam o scraper indisponivel, sendo assim, recomendo que ao verificar que o valor fique indispovível. Alterar o valor pelo o utilizado atualmente.


Executar o script

O script principal para coletar os dados está localizado no arquivo scraper.py.

Personalização:

URL da fonte: A URL do site de onde o valor do dólar será coletado pode ser ajustada diretamente no código, na variável url.
Armazenamento dos dados: Os dados coletados podem ser salvos em um arquivo CSV ou diretamente em um banco de dados. 

