'''
Leia um valor de ponto flutuante com duas casas decimais.
Este valor representa um valor monetário. A seguir,
calcule o menor número de notas e moedas possíveis
no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias
para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
entrada = input()
teste = entrada.split('.')
calculo = int(teste[0])
valor2 = int(teste[1])
nota100, nota50, nota20, nota10, nota5, nota2 = 0, 0, 0, 0, 0, 0
moeda1, moeda50, moeda25, moeda10, moeda5, moeda01 = 0, 0, 0, 0, 0, 0
while calculo > 0:
    if calculo - 100.00 >= 0:
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
    else:
        valor2 = valor2 + 100
        calculo = 0
while valor2 > 0:
    if valor2 - 100 >= 0:
        valor2 = valor2 - 100
        moeda1 += 1
    elif valor2 - 50 >= 0:
        valor2 = valor2 - 50
        moeda50 += 1
    elif valor2 - 25 >= 0:
        valor2 = valor2 - 25
        moeda25 += 1
    elif valor2 - 10 >= 0:
        valor2 = valor2 - 10
        moeda10 += 1
    elif valor2 - 5 >= 0:
        valor2 = valor2 - 5
        moeda5 += 1
    elif valor2 - 1 >= 0:
        valor2 = valor2 - 1
        moeda01 += 1
    else:
        break
print("NOTAS:")
print(f'{nota100} nota(s) de R$ 100.00')
print(f'{nota50} nota(s) de R$ 50.00')
print(f'{nota20} nota(s) de R$ 20.00')
print(f'{nota10} nota(s) de R$ 10.00')
print(f'{nota5} nota(s) de R$ 5.00')
print(f'{nota2} nota(s) de R$ 2.00')
print("MOEDAS:")
print(f'{moeda1} moeda(s) de R$ 1.00')
print(f'{moeda50} moeda(s) de R$ 0.50')
print(f'{moeda25} moeda(s) de R$ 0.25')
print(f'{moeda10} moeda(s) de R$ 0.10')
print(f'{moeda5} moeda(s) de R$ 0.05')
print(f'{moeda01} moeda(s) de R$ 0.01')
