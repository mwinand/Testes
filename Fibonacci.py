# -*- coding: utf-8 -*-
import math

n = int(input("Número para ser usado na sequência de Fibonacci: "))

#Função que retorna se o número recebido é um quadrado perfeito.
def QuadradoPerfeito(x):
    q = int(math.sqrt(x))
    return q*q == x

#Função que retorna True se o número fizer parte da sequência de Fibonacci e False caso não pertença.
def Fibonacci(y):
    return QuadradoPerfeito(5*n*n + 4) or QuadradoPerfeito(5*n*n - 4)

#Execução das funções acima.
if (Fibonacci(n) == True):
    print("O número pertence a sequência de Fibonacci.")
else:
    print("O número não pertence a sequência de Fibonacci.")

