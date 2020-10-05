print('Calcule o quanto de tinta será gasto por m²')
l1 = float(input('Qual é a medida da largura da parede em metros: '))
l2 = float(input('Qual é a medida da altura da parede em metros: '))
m2 = l1 * l2
lpa = 2
print("O Valor Total de Litros de tinta que será gasto é de: {} L".format(m2/lpa))
