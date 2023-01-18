# -*- coding: utf-8 -*-
import json

#Ler arquivo json
f = open('dados.json')
#Carregar Dados
dados = json.load(f)

fatdiario = 0
soma = 0
media = 0
media_dias = 0

#Soma do faturamentos de todos os dias do mês
for i in dados:
  soma = soma + i.get("valor")

#Calcular número de dias em que o faturamento não foi ZERO para calcular a média
for y in dados:
 if y.get("valor") > 0:
     media_dias += 1
     
#print(media_dias)

#Calculo da média mensal
media = soma/media_dias

#Função para encontrar número de dias onde o faturamento foi maior que a média mensal.
for j in dados:
  if j.get("valor") > media:
    fatdiario += 1

#Função para encontrar menor valor de faturamento ocorrido em um dia do mês
menorfat = min(i.get("valor") for i in dados)

#Função para encontrar maior valor de faturamento ocorrido em um dia do mês
maiorfat = max(i.get("valor") for i in dados)

print("Menor valor de faturament ocorrido em um dia do mês:", menorfat)
print("Maior valor de faturament ocorrido em um dia do mês:", maiorfat)
#print(media)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:", fatdiario)


