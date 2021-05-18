'''
Leia 2 valores inteiros (A e B). Após,
o programa deve mostrar uma mensagem "Sao Multiplos"
ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
'''
entrada = input().split()
A, B = int(entrada[0]), int(entrada[1])
if B % A == 0 or A % B == 0:
    print("Sao Multiplos")
else:
    print('Nao sao Multiplos')
