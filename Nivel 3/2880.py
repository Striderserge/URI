texto = input()
segredo = input()

qtd = len(texto) // len(segredo)
diferenca = 1
resultado = 0
while diferenca != 0:
    diferenca = len(texto) - len(segredo)
    teste = texto[0:len(segredo)]
    ponto = 0
    for n in range(len(segredo)):
        if segredo[n] in teste[n]:
            break
        ponto = ponto + 1
    if ponto == len(segredo):
        resultado += 1
    texto = texto[1:]
print(resultado)
