import requests
import pandas as pd
import time
import random
import sqlite3
from bs4 import BeautifulSoup
import datetime
from config import *


for pagina in range(1, paginaLimite +1):
    url = f"{baseUrl}?page{pagina}"

    # ( e.g. https://www.adorocinema.com/filmes/melhores/?page=2 )
    print(f"Coletando dados da pagina {pagina} \n URL: {url}")
    resposta = requests.get(url, headers=headers)

    if resposta.status_code != 200:
        print(f'Erro ao carregar a pagina {pagina}. Codigo do erro é: {resposta.status_code}')

    soup = BeautifulSoup(resposta.text, "html.parser")
    cards = soup.find_all("div", class_ = "card entity-card entity-card-list cf")

    for card in cards:
        try:
            # tenta capturar o titulo do filme e o hiperlink da pagina
            titulo_tag = card.find('a', class_ = "meta-title-link")
            titulo = titulo_tag.text.strip() if titulo_tag else "N/A"
            link = "https://www.adorocinema.com/filmes/" + titulo_tag['href'] if titulo_tag else None

            # captura a nota do filme
            nota_tag = card.find("span", class_ = "stareval-note")
            nota = nota_tag.text.strip().replace(',','.') if nota_tag else "N/A"

            if link:
                filme_resposta = requests.get(link, headers=headers)
                
                if resposta.status_code != 200:
                    filme_soup = BeautifulSoup(filme_resposta.text, "html.parser")

                    diretor_tag = filme_soup.find("div", class_ = "meta-body-item meta-body-direction meta-body-oneline")
                    if diretor_tag:
                        diretor = diretor_tag.text.strip().replace('Direção',',').replace(',','').replace('|','').replace('\n','').replace('\r',',').strip()
                        genero_block = filme_soup.find('div', class_ = 'meta-body-info')
                if genero_block:
                    genero_link = genero_block.find_all('a')
                    generos = [g.text.strip() for g in genero_link]
                    categoria = ", ".join(generos[:3]) if generos else "N/A"
                else:
                    categoria = "N/A"

        except Exception as erro:
            print(f"Erro ao processar o filme {titulo}. Erro: {erro}")