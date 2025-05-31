import os
import django

# Aqui você coloca o nome do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  
django.setup()

from data.models import MaioresDividendos
import json
from pathlib import Path

from decimal import Decimal

# Como o script está na raiz, o JSON fica em: data/json/Maiores_Dividend.json
caminho_arquivo = Path('data') / 'json' / 'Maiores_Dividend.json'

with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    dados = json.load(file)

for item in dados:
    MaioresDividendos.objects.create(
        codigo=item['codigo'],
        dividendo_atual=Decimal(item['dividendo_atual']),
        dividendo_medio=Decimal(item['dividendo_medio']),
        p_l=Decimal(item['p_l']),
        p_vp=Decimal(item['p_vp']),
        margem_liquida=Decimal(item['margem_liquida']),
        #valor_mercado=Decimal(item['valor_mercado']),
        setor=item['setor'],
        data=item['data']
    )

print("Importação concluída.")