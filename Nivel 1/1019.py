'''
Leia um valor inteiro, que é o tempo de duração em segundos
de um determinado evento em uma fábrica, e informe-o expresso
no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos),
convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''
entrada = int(input())
hora, minuto, segundo = 0, 0, 0
while entrada > 0:
    if entrada - 3600 >= 0:
        entrada = entrada - 3600
        hora += 1
    elif entrada - 60 >= 0:
        entrada = entrada - 60
        minuto += 1
    else:
        segundo = entrada
        entrada = 0
print(f'{hora}:{minuto}:{segundo}')
