'''
Leia 4 valores inteiros A, B, C e D.
A seguir, se B for maior do que C e se D for maior do que A,
e a soma de C com D for maior que a soma de A e B e se C e D,
ambos, forem positivos e se a variável
A for par escrever a mensagem "Valores aceitos",
senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.
'''
entrada = input().split()
A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])
if B > C:
    if D > A:
        if (C + D) > (A + B):
            if C > 0 and D > 0:
                if A % 2 == 0:
                    print('Valores aceitos')
                else:
                    print('Valores nao aceitos')
            else:
                print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')
else:
    print('Valores nao aceitos')
