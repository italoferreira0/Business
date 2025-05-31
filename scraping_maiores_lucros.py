import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from datetime import date

url = "https://investidor10.com.br/acoes/rankings/maiores-lucros/"

email = "italofsilva583@outlook.com"
senha = "Italo8642@"

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

buttonDnv = driver.find_element(By.CSS_SELECTOR, 'button[data-id="read-more-action"]')
buttonDnv.click()

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
        "Cota": dado[0],
        "LUCRO": dado[1],
        "P/L": dado[2],
        "P/PV": dado[3],
        "Margem Liquida": dado[4],
        "Valor de Mercado": dado[5],
        "DY Medio(5 anos)": dado[6],
        "Setor": dado[7],
        "Data": data_format
    }   

    dados.append(objeto)

dados.pop(0)
(len(dados))

caminho_arquivo = 'json/Rankings_Maiores_Lucros.json'

with open(caminho_arquivo, 'w') as f:
    json.dump(dados, f, indent=4)

driver.quit()