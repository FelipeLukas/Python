menor = 2**31-1
soma = 0

for i in range (5):
    n=int(input('Digite um numero inteiro: '))
    soma += n
    if n < menor:
        menor = n
print (f"A soma dos valores apresentados foi: {soma}")
print (f"O menor numero informado foi:  {menor}") 