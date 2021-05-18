import math
'''
Leia 3 valores de ponto flutuante e efetue o
cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes,
mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes,
apresente a mensagem "Impossivel calcular".
Caso contrário,
imprima o resultado das raízes com 5 dígitos após o ponto,
com uma mensagem correspondente conforme exemplo abaixo.
Imprima sempre o final de linha após cada mensagem.
'''
entrada = input().split()
A, B, C = float(entrada[0]), float(entrada[1]), float(entrada[2])
delta = math.pow(B, 2) - 4 * A * C
if delta > 0 and A != 0:
    x1 = (B * (-1) + math.sqrt(delta)) / (2 * A)
    x2 = (B * (-1) - math.sqrt(delta)) / (2 * A)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
else:
    print('Impossivel calcular')
