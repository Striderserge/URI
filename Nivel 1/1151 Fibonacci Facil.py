'''
A seguinte sequência de números 0 1 1 2 3 5 8 13 21...
é conhecida como série de Fibonacci.
Nessa sequência, cada número, depois dos 2 primeiros,
é igual à soma dos 2 anteriores.
Escreva um algoritmo que leia um inteiro N (N < 46)
e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha,
separados por um espaço em branco.
Não deve haver espaço após o último valor.
'''
n1 = 0
n2 = 1
cont = int(input())
for i in range(1, cont+1):
    if i % cont == 0:
        print(n1)
    else:
        print(n1, end=' ')
    soma = n1 + n2
    n1 = n2
    n2 = soma
