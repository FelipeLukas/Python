#neste exercicio o professor nos provocou a explorar o lado voltado ao visual e essa brincadeira com a programação
#tendo como objetivo criar uma especie de arvore de natal
#perceba: se alterarmos o 'x', teremos mais camadas nesta arvore virtual pixelada


#variaveis
x = 10
y= 1

#programa
for i in range(x):
    for j in range(y):
        print('*', end="")
    y += 1
    print()

