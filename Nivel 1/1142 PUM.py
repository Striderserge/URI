'''
Escreva um programa que leia um valor inteiro N.
Este N é a quantidade de linhas de saída que serão
apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
'''
linha = 1
cont = 1
entrada = int(input())
while linha <= entrada:
    if cont % 4 != 0:
        print(cont, end=' ')
    else:
        print('PUM')
        linha += 1
    cont += 1
