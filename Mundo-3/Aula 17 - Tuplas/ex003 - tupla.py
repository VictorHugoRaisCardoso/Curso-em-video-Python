from random import randint

menor = maior = int
sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for i in sorteados:
    print(f"{i}", end=" ")
print()
menor = maior = sorteados[0]
for i in sorteados:
    if i < menor:
        menor = i
    elif i > maior:
        maior = i
print(f"O maior numero gerado foi: {maior}.")
print(f"O menor numero gerado foi: {menor}.")
