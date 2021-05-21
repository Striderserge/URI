'''
Você deve fazer um programa que apresente a sequencia
conforme o exemplo abaixo.

I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
'''
i = 0
j = 1
conta = 0
bonus = 0.2
x = 1
while i <= 2:
    if x <= 3:
        print(f'I={i:.0f} J={j:.0f}')
    else:
        print(f'I={i:.1f} J={j:.1f}')
    x += 1
    if x > 15:
        x = 1
    j += 1
    conta += 1
    if conta == 3:
        j -= 3
        i += bonus
        j += bonus
        conta = 0
