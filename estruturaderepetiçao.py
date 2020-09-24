total = mulher = homem = 0
condição = 1

while condição != 0:
    sexo = input("Digite um Sexo (M ou F) ou 0 para revisar o total: ")
    sexo = sexo.upper()
    if sexo in "MF":
        total += 1

        if sexo == "M":
            homem += 1
        else:
            mulher += 1

    else:
        print('O total de pessoas do sexo masculino : {}'.format(homem))
        print('O total de pessoas do sexo feminino  : {}'.format(mulher))
        print('O total de pessoas do inteiro grupo  : {}'.format(total))
        exit()



