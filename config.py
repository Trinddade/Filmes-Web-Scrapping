#  ___            _     _ _     _        ____                       
# |_ _|_ ____   _(_)___(_) |__ | | ___  / ___|  ___ _ __ __ _ _ __  
#  | || '_ \ \ / / / __| | '_ \| |/ _ \ \___ \ / __| '__/ _` | '_ \ 
#  | || | | \ V /| \__ \ | |_) | |  __/  ___) | (__| | | (_| | |_) |
# |___|_| |_|\_/ |_|___/_|_.__/|_|\___| |____/ \___|_|  \__,_| .__/ 
# |  \/  | _____   _(_) ___  ___                             |_|    
# | |\/| |/ _ \ \ / / |/ _ \/ __|                                   
# | |  | | (_) \ V /| |  __/\__ \                                   
# |_|  |_|\___/ \_/ |_|\___||___/                                   
#
# Versão : 1.0
# Data : 27-02-2026
# Autor : Lucas Trindade

import datetime

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36'
}

baseUrl = "https://www.adorocinema.com/filmes/melhores/"
filmes = []

data_hoje = datetime.date.today().strftime("%d-%m-%Y")
inicio = datetime.datetime.now()

card_temp_min = 1
card_temp_max = 3
pag_temp_min = 2
pag_temp_max = 4
paginaLimite = 5
bancoDados = "filmes.db"
saidaCSV = f"filmes_adorocinema_{data_hoje}.csv"