## Sobre

Repositório para a APS01 da cadeira de Natural Language Processing, eletiva no Insper.

Você já tentou procurar um jogo de um tema específico, mas nunca um jogo combina perfeitamente com sua busca? Esse projeto busca resolver esse problema.

Queries devem ser feitas com palavras em inglês, separando palavras com hífens em vez de espaços.

Exemplos:
- Quero um jogo mundo aberto com temática de pirata -> .../query?query=open-world-pirate
- Quero um jogo com apocalipse zumbi -> .../query?query=zombie-apocalypse
- Quero um jogo shooter em primeira pessoa com tema futurístico -> .../query?query=futuristic-first-person-shooter

Usa um dabatase de jogos da steam, obtida pelo scrapper https://github.com/FronkonGames/Steam-Games-Scraper

## Uso

Como rodar localmente (guia para Windows):
- Clone o repositório
- Entre na pasta do repositório
- Crie uma env `python venv env`
- Ative a env `env/Scripts/activate`
- Instale as bibliotecas `python -m pip install -r requirements.txt`
- Abra um terminal no repositório e rode `python app.py`
- Entre no link que aparece no terminal e divirta-se!

## Para entrega: 

Test that yields 10 results: http://10.103.0.28:7591/query?query=open-world-pirate-game


Test that yields less than 10 results: http://10.103.0.28:7591/query?query=principle


Test that yields something non-obvious: http://10.103.0.28:7591/query?query=not-bloody

O resultado da query 'not bloody' encontra vários jogos muito sangrentos! Isso ocorre pois o modelo não entende o que a query está dizendo, apenas busca as palavras na query sem contexto.