'''
Leia um valor inteiro correspondente à idade
de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo
ano com 365 dias e todo mês com 30 dias. Nos casos de teste
nunca haverá uma situação que permite 12 meses e alguns dias,
como 360, 363 ou 364. Este é apenas um exercício com objetivo de
testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
'''
entrada = int(input())
ano, meses, dia = 0, 0, 0
while entrada > 0:
    if entrada - 365 >= 0:
        ano += 1
        entrada = entrada - 365
    elif entrada - 30 >= 0:
        meses += 1
        entrada = entrada - 30
    else:
        dia = entrada
        entrada = 0
print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dia} dia(s)')
