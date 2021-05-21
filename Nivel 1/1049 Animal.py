'''
Neste problema, você deverá ler 3 palavras que definem
o tipo de animal possível segundo o esquema abaixo,
da esquerda para a direita.
Em seguida conclua qual dos animais seguintes foi escolhido,
através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha,
necessárias para identificar o animal segundo a figura acima,
com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''
osso = input()
classe = input()
comida = input()

if osso == 'vertebrado':
    if classe == 'ave':
        if comida == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if comida == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if classe == 'inseto':
        if comida == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if comida == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
