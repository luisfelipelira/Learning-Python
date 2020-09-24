vitoria = int(input('Digite o número de jogos vitoriosos: '))
empate = int(input('Digite o número de empates: '))
derrota = int(input('Digite o número de derrotas: '))
jogos = vitoria + empate + derrota
pontos_ganhos = vitoria*3
perdidos = derrota*3 + empate*2
print('O time jogou {} jogos e obteve {} pontos e teve {} pontos peridos'.format(jogos, pontos_ganhos, perdidos))

