tamanho = 4
soma = media = 0.0
numero = [] #lista de números

for ind in range(tamanho):
    numero.append(int(input(f'Digite um valor para a Posição {ind+1}: ')))
    soma += numero[ind]

media = soma/tamanho

print('-=' * 15)
print(f'Media dos valores: {media}')