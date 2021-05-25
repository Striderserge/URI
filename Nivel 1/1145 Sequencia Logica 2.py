'''
Escreva um programa que leia dois valores X e Y.
A seguir, mostre uma sequência de 1 até Y,
passando para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros,
(1 < X < 20) e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas,
com 1 espaço em branco entre cada número, conforme exemplo abaixo.
Não deve haver espaço em branco após o último valor da linha.
'''
entrada = input().split()
linha, fim = int(entrada[0]), int(entrada[1])
for i in range(1, fim+1):
    if i % linha == 0:
        print(i)
    else:
        print(i, end=' ')
