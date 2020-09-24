descri = input('Digite o nome do produto: ')
preco = float(input('Digite o preço a se pagar pela unidade: '))
quantidade = int(input('Qual a quantidade você deseja comprar: '))
print('Você escolheu o produto {} no qual você informou que custa {} reais e você deseja comprar {} '
      .format(descri, preco, quantidade))
print('Você deverá pagar {} reais no total produto escolhido'.format(preco*quantidade))
