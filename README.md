# Web Scraping de Filmes

Este projeto realiza **web scraping no site AdoroCinema** para coletar informações sobre filmes e armazenar esses dados para análise.

O script navega automaticamente pelas páginas do site, coleta dados de cada filme e organiza essas informações em um **arquivo CSV** e em um **banco de dados SQLite**.

## Dados coletados

Durante o processo de coleta, o script captura as seguintes informações:

* Título do filme
* Diretor
* Nota do filme
* Link da página do filme
* Ano de lançamento
* Categoria / Gênero

Esses dados podem ser utilizados posteriormente para **análise exploratória, visualização de dados ou criação de dashboards**.

## Tecnologias utilizadas

* **Python**
* **Requests** – requisições HTTP
* **BeautifulSoup** – extração de dados do HTML
* **Pandas** – manipulação e estruturação dos dados
* **SQLite** – armazenamento em banco de dados

## Estrutura do projeto

```
📁 projeto
│
├── main.py
├── config.py
├── grafico_ws.py
├── filmes.db
├── filmes_adorocinema_02-03-2026.csv
└── README.md
```

**Descrição dos arquivos**

* `main.py` → script principal responsável pelo web scraping
* `config.py` → configurações do projeto (URL base, limites de páginas, headers etc.)
* `grafico_ws.py` → geração de gráficos a partir dos dados coletados
* `filmes.db` → banco de dados SQLite com os filmes coletados
* `filmes_adorocinema_02-03-2026.csv` → dataset gerado após a coleta
* `README.md` → documentação do projeto

## Como executar o projeto

Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Instale as dependências:

```
pip install requests pandas beautifulsoup4
```

Execute o script principal:

```
python main.py
```

Após a execução, os dados coletados serão salvos automaticamente em **CSV e SQLite**.

## Objetivo do projeto

Este projeto foi desenvolvido para praticar conceitos importantes de **engenharia e análise de dados**, incluindo:

* Web Scraping
* Coleta automatizada de dados
* Estruturação de dados
* Processos de ETL (Extração, Transformação e Carga)
* Armazenamento em banco de dados
