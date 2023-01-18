# -*- coding: utf-8 -*-
n = input("Insira uma palavra ou frase para que seja invertida. ")

def Inverter_String(text):
    invertida = ""
    for char in text:
        invertida = char + invertida
    return invertida

print (Inverter_String(n))
    

