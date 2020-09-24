"""" FAÇA UM PROGRAMA QUE OBTENHA A PARTIR DA DIGITAÇÃO DO USUÁRIO OS SEGUINTES DADOS: A QUANTIDADE DE ALUNOS QUE
FAZEM O CURSO DE SISTEMAS DE INFORMAÇÃO E A QUANTIDADE DE ALUNOS QUE FAZEM O CURSO DE ANÁLISE DE SISTEMAS. AO FINAL O
PROGRAMA DEVE INFORMAR O TOTAL DE ALUNOS, A PORCENTAGEM DE ALUNOS QUE FAZEM SISTEMAS E A PORCENTAGEM DE ALUNOS QUE
CURSAM ANÁLISES. """
si = int(input('Quantos alunos Fazem o Curso de Sistemas de Informações? '))
ansi = int(input('Quantos alunos Fazem o Curso de Análise de Sistemas? '))
total = ansi + si
print('{}% fazem o Curso de Sistemas de informações e {}% fazem Análise de Sistemas.'.format(si*100/total, ansi*100/total))
