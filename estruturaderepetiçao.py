total = mulher = homem = 0
condicao = 1

while condicao != 0:
    sexo = input("Digite um Sexo (M ou F) ou pressione apenas enter para revisar o total: ")
    sexo = sexo.upper()
    if sexo in "MF":
        total += 1

        if sexo == "M":
            homem += 1
        elif sexo == "F":
            mulher += 1
        else:
            print('O total de pessoas do sexo feminino  : {}'.format(mulher))
            print('O total de pessoas do sexo masculino : {}'.format(homem))
            print('O total de pessoas do inteiro grupo  : {}'.format(total-1))
            exit()

    else:
        print('Opção Inválida')
