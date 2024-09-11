# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.

numero = int(input("digite o numero para saber se é par ou impar: "))

valor = numero %2
if (valor == 0):
    print("numero é par")
else:
    print("numero é impar")
