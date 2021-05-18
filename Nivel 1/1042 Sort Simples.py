'''
Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida,
os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''
lista1 = input().split()
for i in range(len(lista1)):
    lista1[i] = int(lista1[i])
lista2 = sorted(lista1)
for item in lista2:
    print(item)
print()
for item in lista1:
    print(item)
