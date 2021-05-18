import math
'''
Faça um programa que leia três valores e apresente o maior
dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço
e a mensagem "eh o maior".
'''

dados = input().split()
v1 = int(dados[0])
v2 = int(dados[1])
v3 = int(dados[2])
if v1 > v2 and v1 > v3:
    print(f'{v1} eh o maior')
if v2 > v1 and v2 > v3:
    print(f'{v2} eh o maior')
if v3 > v1 and v3 > v2:
    print(f'{v3} eh o maior')

valor = input().split(" ")

a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b))) / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print("%d eh o maior" % resultado)
