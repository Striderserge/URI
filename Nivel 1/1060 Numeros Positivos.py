'''
Faça um programa que leia 6 valores.
Estes valores serão somente negativos ou positivos
(desconsidere os valores nulos). A seguir,
mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''
positivos = 0
numeros = []
for i in range(6):
    numeros.append(float(input()))
for item in numeros:
    if item >= 0:
        positivos += 1
print(f'{positivos} valores positivos')
