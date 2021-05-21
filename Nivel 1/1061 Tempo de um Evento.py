'''
Pedrinho está organizando um evento em sua Universidade.
O evento deverá ser no mês de Abril,
iniciando e terminando dentro do mês.
O problema é que Pedrinho quer calcular o tempo que o evento vai durar,
uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias,
você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”,
seguido de um espaço e o dia do mês no qual o evento vai começar.
Na linha seguinte, será informado o momento no qual o evento vai iniciar,
no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra
informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema
tem duração mínima de 1 minuto.
'''
dia, hora, minuto, segundo = 0, 0, 0, 0
entrada = input().split()
diainicio = int(entrada[1])
entrada = input().split()
horainicio, minutoinicio, segundoinicio = int(entrada[0]), int(entrada[2]), int(entrada[4])
entrada = input().split()
diafim = int(entrada[1])
entrada = input().split()
horafim, minutofim, segundofim = int(entrada[0]), int(entrada[2]), int(entrada[4])

if segundoinicio > segundofim:
    segundo = 60 - segundoinicio + segundofim
    minutofim += -1
else:
    segundo = segundofim - segundoinicio
if segundo >= 60:
    segundo -= 60
    minuto += 1
if minutoinicio > minutofim:
    minuto += 60 - minutoinicio + minutofim
    horafim += -1
else:
    minuto += minutofim - minutoinicio
if minuto >= 60:
    minuto -= 60
    hora += 1
if horainicio > horafim:
    hora += 24 - horainicio + horafim
    dia += -1
else:
    hora += horafim - horainicio
if hora >= 24:
    hora -= 24
    dia += 1
dia += diafim - diainicio
print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')
