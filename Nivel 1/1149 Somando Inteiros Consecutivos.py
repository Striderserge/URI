'''
Faça um algoritmo para ler um valor A e um valor N.
Imprimir a soma de A para cada i com os valores (0 <= i <= N-1).
Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos.
Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.
'''
entrada = input().split()
n1 = int(entrada[0])
n2 = int(entrada[-1])
soma = 0
for i in range(n2):
    soma += i + n1
print(soma)
