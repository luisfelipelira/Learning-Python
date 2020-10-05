matriz = [[0, 0], [0, 0]] # matriz com duas linhas e duas colunas
soma = 0
for linha in range(2): # controla a linha da matriz
    for coluna in range(2): # controla a coluna da matriz
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        soma += matriz[linha][coluna]

print('-=' * 20)
for linha in range(2):
    for coluna in range(2):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 20)
print(f'Soma dos valores da matriz: {soma}', end='')