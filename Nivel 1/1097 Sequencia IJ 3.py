'''
Você deve fazer um programa que apresente a
sequencia conforme o exemplo abaixo.
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
'''
i = 1
j = 7
corte = 5
while i <= 9:
    print(f'I={i} J={j}')
    j -= 1
    if j < corte:
        i += 2
        j += 5
        corte += 2
