# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.

número = float(input('Digite um número para saber se é par ou impar: '))
resto = número % 2

if resto == 0:
    print('Número é par')

else:
    print('Número é impar')