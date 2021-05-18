'''
Leia a hora inicial, minuto inicial,
hora final e minuto final de um jogo.
A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''
entrada = input().split()
horainicial = int(entrada[0])
minutoinicial = int(entrada[1])
horafinal = int(entrada[2])
minutofinal = int(entrada[3])
hora = 0
minuto = 0
if horafinal == horainicial and minutofinal == minutoinicial:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif horafinal == horainicial and minutofinal != minutoinicial:
    if minutoinicial > minutofinal:
        minuto = 60 - minutoinicial + minutofinal
        print(f'O JOGO DUROU 23 HORA(S) E {minuto} MINUTO(S)')
    else:
        print(f'O JOGO DUROU 0 HORA(S) E {minutofinal-minutoinicial} MINUTO(S)')
else:
    if minutoinicial > minutofinal:
        minuto = 60 - minutoinicial + minutofinal
        if horainicial > horafinal:
            hora = 24 - horainicial + horafinal - 1
        else:
            hora = horafinal - horainicial - 1
    else:
        if horainicial > horafinal:
            hora = 24 - horainicial + horafinal
        else:
            hora = horafinal - horainicial
        minuto = minutofinal - minutoinicial
    print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
