'''
Leia a hora inicial e a hora final de um jogo.
A seguir calcule a duração do jogo,
sabendo que o mesmo pode começar em um dia e terminar em outro,
tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início
e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
'''
entrada = input().split()
comeco, final = int(entrada[0]), int(entrada[1])
if comeco < final:
    print(f'O JOGO DUROU {final - comeco} HORA(S)')
elif comeco == final:
    print('O JOGO DUROU 24 HORA(S)')
else:
    print(f'O JOGO DUROU {24 - comeco + final} HORA(S)')
