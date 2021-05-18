'''
Leia um valor inteiro. A seguir, calcule o menor número de
notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a
quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de
linha após cada linha, caso contrário seu programa
apresentará a mensagem: “Presentation Error”.
'''
entrada = int(input())
nota100, nota50, nota20, nota10, nota5, nota2, nota1 = 0, 0, 0, 0, 0, 0, 0
print(entrada)
calculo = entrada
while calculo > 0:
    if calculo - 100 >= 0:
        calculo = calculo - 100
        nota100 += 1
    elif calculo - 50 >= 0:
        calculo = calculo - 50
        nota50 += 1
    elif calculo - 20 >= 0:
        calculo = calculo - 20
        nota20 += 1
    elif calculo - 10 >= 0:
        calculo = calculo - 10
        nota10 += 1
    elif calculo - 5 >= 0:
        calculo = calculo - 5
        nota5 += 1
    elif calculo - 2 >= 0:
        calculo = calculo - 2
        nota2 += 1
    elif calculo - 1 >= 0:
        calculo = calculo - 1
        nota1 += 1
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')
