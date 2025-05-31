import os
import django

# Aqui você coloca o nome do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  
django.setup()

#Web scripts
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from datetime import date

# Imports
from data.models import MaioresLucros
import json
from pathlib import Path
from decimal import Decimal

url = "https://investidor10.com.br/acoes/rankings/maiores-lucros/"

email = "italofsilva583@outlook.com"
senha = "Italo8642@"

hoje = str(date.today())
data_atual = str(date.today()).split('-')
data_format = f'{data_atual[2]}-{data_atual[1]}-{data_atual[0]}'

option = Options()
driver = webdriver.Chrome(options=option)

driver.get(url)
time.sleep(10)

for _ in range(1):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="read-more-action"]')
button.click()

time.sleep(5)
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(email)

senha_input = driver.find_element(By.NAME, "password")
senha_input.send_keys(senha)

botao_entrar = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Entrar"]')
botao_entrar.click()

time.sleep(5)

for _ in range(1):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)

time.sleep(5)

button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="read-more-action"]')
button.click()

time.sleep(5)

for _ in range(1):
    driver.execute_script("window.scrollBy(0, -500);")
    time.sleep(1)

time.sleep(5)

filtro = driver.find_element(By.CSS_SELECTOR, 'th[data-name="name_sector"]')
filtro.click()

time.sleep(5)

table_element = driver.find_element(By.ID, "rankigns")

linhas = table_element.find_elements(By.TAG_NAME, "tr")

dados = []

for linha in linhas:
    colunas = linha.find_elements(By.XPATH, ".//th | .//td")
    dado = [coluna.text.strip() for coluna in colunas]
    
    objeto = {
        "codigo": dado[0],
        "lucro": dado[1],
        "p_l": dado[2].replace('%','').replace(',','.'),
        "p_vp": dado[3].replace('%','').replace(',','.'),
        "margem_liquida": dado[4].replace('%','').replace(',','.'),
        #"valor_mercado": dado[5].replace('%','').replace(' ','').replace('B','').replace(',','.'),"Valor de Mercado": dado[5],
        "dividendo_medio": dado[6].replace('%','').replace(',','.'),
        "setor": dado[7],
        "data": hoje
    }   

    dados.append(objeto)

dados.pop(0)
(len(dados))

caminho_arquivo = 'data/json/Maiores_Lucros.json'

with open(caminho_arquivo, 'w') as f:
    json.dump(dados, f, indent=4)

driver.quit()

caminho_arquivo = Path('data') / 'json' / 'Maiores_Lucros.json'

with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    dados = json.load(file)

for item in dados:
    MaioresLucros.objects.create(
        codigo=item['codigo'],
        lucro=(item['lucro']),
        p_l=Decimal(item['p_l']),
        p_vp=Decimal(item['p_vp']),
        margem_liquida=Decimal(item['margem_liquida']),
        dividendo_medio=Decimal(item['dividendo_medio']),
        #valor_mercado=Decimal(item['valor_mercado']),
        setor=item['setor'],
        data=item['data']
    )

print("Importação concluída.")


