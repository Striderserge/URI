'''
Maria acabou de iniciar seu curso de graduação na faculdade
de medicina e precisa de sua ajuda para organizar os experimentos
de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
quantas cobaias foram utilizadas no laboratório e o percentual
de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos,
ratos e coelhos. Para obter estas informações, ela sabe exatamente o
número de experimentos que foram realizados, o tipo de cobaia utilizada
e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários
casos de teste que vem a seguir. Cada caso de teste contém um
inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de
cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o
tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de
cobaia utilizada e o percentual de cada uma em relação ao total de cobaias
utilizadas, sendo que o percentual deve ser apresentado com
dois dígitos após o ponto.
'''
dados = {}
for i in range(int(input())):
    entrada = input().split()
    if entrada[1] not in dados:
        dados[entrada[1]] = int(entrada[0])
    else:
        dados[entrada[1]] += int(entrada[0])
total = 0
for item in dados:
    total += dados[item]
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {dados["C"]}')
print(f'Total de ratos: {dados["R"]}')
print(f'Total de sapos: {dados["S"]}')
print(f'Percentual de coelhos: {dados["C"]/total*100:.2f} %')
print(f'Percentual de ratos: {dados["R"]/total*100:.2f} %')
print(f'Percentual de sapos: {dados["S"]/total*100:.2f} %')
