'''
Escreva um algoritmo para calcular e escrever o valor de S,
sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
'''
total = 1
i = 1
j = 1
while True:
    total = total + (i + 2) / (j*2)
    i += 2
    j = j * 2
    if i == 39:
        break
print(f'{total:.2f}')
