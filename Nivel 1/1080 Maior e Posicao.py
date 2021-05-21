'''
Leia 100 valores inteiros.
Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
maior, pos = 0, 0
for i in range(100):
    dado = int(input())
    if dado > maior:
        maior = dado
        pos = i
print(maior)
print(pos)
