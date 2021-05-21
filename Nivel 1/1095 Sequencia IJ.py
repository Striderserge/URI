'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo
abaixo.
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo
'''

i = 1
j = 60
for j in range(j, -2, -5):
    print(f'I={i} J={j}')
    i += 3
