import requests
import pandas as pd
import time
import random
import sqlite3
from bs4 import BeautifulSoup
import datetime
from config import *


for pagina in range(1, paginaLimite +1):
    url = f"{baseUrl}?page={pagina}"

    # ( e.g. https://www.adorocinema.com/filmes/melhores/?page=2 )
    print(f"Coletando dados da pagina {pagina} \n URL: {url}")
    resposta = requests.get(url, headers=headers)

    if resposta.status_code != 200:
        print(f'Erro ao carregar a pagina {pagina}. Codigo do erro é: {resposta.status_code}')

    soup = BeautifulSoup(resposta.text, "html.parser")
    cards = soup.find_all("div", class_ = "card entity-card entity-card-list cf")

    for card in cards:
        genero_block = None
        diretor = "N/A"
        categoria = "N/A"
        ano = "N/A"

        try:
            # tenta capturar o titulo do filme e o hiperlink da pagina
            titulo_tag = card.find('a', class_ = "meta-title-link")
            titulo = titulo_tag.text.strip() if titulo_tag else "N/A"
            link = "https://www.adorocinema.com" + titulo_tag['href'] if titulo_tag else None

            # captura a nota do filme
            nota_tag = card.find("span", class_ = "stareval-note")
            nota = nota_tag.text.strip().replace(',','.') if nota_tag else "N/A"

            if link:
                filme_resposta = requests.get(link, headers=headers)
                
                if filme_resposta.status_code == 200:
                    filme_soup = BeautifulSoup(filme_resposta.text, "html.parser")

                    diretor_tag = filme_soup.find("div", class_ = "meta-body-item meta-body-direction meta-body-oneline")
                    if diretor_tag:
                        diretor_texto = diretor_tag.text.strip().replace('Direção',',').replace(',','').replace(':','').replace('|','').replace('\n','').replace('\r',',').strip()
                        diretor = " ".join(diretor_texto.split())
                        genero_block = filme_soup.find('div', class_ = 'meta-body-info')

                if genero_block:
                    ano_tag = genero_block.find('span', class_ = 'date')
                    ano = ano_tag.text.strip() if ano_tag else "N/A"
                    partes = genero_block.text.split('|')
                    if len(partes) > 0:
                        texto_categoria = partes[-1]
                        categoria = " ".join(texto_categoria.split())
                    else:
                        categoria = "N/A"
                else:
                    categoria = "N/A"
                    ano = "N/A"

                # só adiciona o filme se todos os dados principais existirem
                if titulo != 'N/A' and link != 'N/A' and nota != 'N/A':
                    filmes.append({
                        'Titulo': titulo,
                        'Direcao': diretor,
                        'Nota': nota,
                        'Link': link,
                        'Ano': ano,
                        'Categoria': categoria
                    })
                else: print(f'Filme incompleto ou erro na coleta de dados.')

                # espera um tempo entre os cartões para não sobrecarregar o site
                tempo = random.uniform(card_temp_min, card_temp_max)
                time.sleep(tempo)
                print(f'Tempo de espera: {tempo}s')

        except Exception as erro:
            print(f"Erro ao processar o filme {titulo}. Erro: {erro}")

    # espera um tempo aleatório entre as páginas para não sobrecarregar o site
    tempo = random.uniform(card_temp_min, card_temp_max)
    time.sleep(tempo)
    print(f'Pagina: Tempo de espera: {tempo}s')

df = pd.DataFrame(filmes)
print(df.head())

df.to_csv(saidaCSV, index=False, encoding='utf-8-sig', quotechar="'", quoting=1)

conn = sqlite3.connect(bancoDados)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS filmes")
cursor.execute('''
               CREATE TABLE IF NOT EXISTS filmes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Titulo TEXT,
               Direcao TEXT,
               Nota REAL,
               Link TEXT,
               Ano TEXT,
               Categoria TEXT
               )
    ''')

for filme in filmes:
    try:
        cursor.execute('''
        INSERT INTO filmes
            (Titulo, Direcao, Nota, Link, Ano, Categoria)
        VALUES
            (?,?,?,?,?,?)
        ''',(
            filme['Titulo'],
            filme['Direcao'],
            float(filme['Nota']) if filme['Nota'] != 'N/A' else None,
            filme['Link'],
            filme['Ano'],
            filme['Categoria']
        ))
    except Exception as erro:
        print(f"Erro ao inserir filme {filme['Titulo']} no banco de dados. Codigo do erro:{erro}")
conn.commit()
conn.close()

agora = datetime.datetime.now()
print('------------------------------------------------------------')
print('Dados raspados e salvos com sucesso')
print(f'Arquivo salvo em {saidaCSV}')
print('Obrigado por usar o script de WebScrapping do Lucas')
print(f'Finalizado em {agora.strftime("%H:%M:%S")}')
print('------------------------------------------------------------')