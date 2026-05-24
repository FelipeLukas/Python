#o objetivo deste exercicio é contar quantas vezes a letra "a" minúscula se repete na palavra informada pelo usuário

#variaveis
contador=0

#programa
p=input('Por favor, digite qualquer palavra: ')
for i in p:
    if i == 'a':
        contador += 1
print(f'Número de vezes em que "a" se repetiu: {contador}')
