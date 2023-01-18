# -*- coding: utf-8 -*-
import json

total = 0
porcentagem = 0
estado = ""

#Ler arquivo json
f = open('distribuidora.json')
#Carregar Dados
dados = json.load(f)

#Calcula valor total do faturamento da distribuidora
for i in dados:
    total = total + i.get("valor")

#Calcula porcentagem de cada estado e retorna para o usuario a porcentagem ao lado do nome do estado
for j in dados:
    porcentagem = (j.get("valor") / total) * 100
    estado = j.get("estado")
    print(estado, round(porcentagem, 2),"%")
