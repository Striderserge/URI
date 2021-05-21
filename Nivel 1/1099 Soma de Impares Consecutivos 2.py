'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste de dois inteiros X e Y.
Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a
quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
'''
soma = 0
for i in range(int(input())):
    entrada = input().split()
    if int(entrada[1]) > int(entrada[0]):
        for i in range(int(entrada[0])+1, int(entrada[1])):
            if i % 2 != 0:
                soma += i
    else:
        for i in range(int(entrada[1])+1, int(entrada[0])):
            if i % 2 != 0:
                soma += i
    print(soma)
    soma = 0
