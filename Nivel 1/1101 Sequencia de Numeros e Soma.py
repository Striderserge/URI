'''
Leia um conjunto não determinado de pares de valores M e N
(parar quando algum dos valores for menor ou igual a zero).
Para cada par lido, mostre a sequência do menor até o maior e
a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N.
A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a
soma deles, conforme exemplo abaixo.
'''
soma = 0
while True:
    entrada = input().split()
    if int(entrada[1]) <= 0 or int(entrada[0]) <= 0:
        break
    if int(entrada[0]) > int(entrada[1]):
        for i in range(int(entrada[1]), int(entrada[0])+1):
            print(i, end=' ')
            soma += i
        print(f'Sum={soma}')
    else:
        for i in range(int(entrada[0]), int(entrada[1])+1):
            print(i, end=' ')
            soma += i
        print(f'Sum={soma}')
    soma = 0
