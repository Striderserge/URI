'''
Leia 5 valores Inteiros. A seguir mostre quantos
valores digitados foram pares, quantos valores digitados foram ímpares,
quantos valores digitados foram positivos
e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido,
uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''
par, impar, positivo, negativo = 0, 0, 0, 0
for i in range(5):
    dado = int(input())
    if dado % 2 == 0:
        par += 1
    else:
        impar += 1
    if dado > 0:
        positivo += 1
    elif dado < 0:
        negativo += 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
