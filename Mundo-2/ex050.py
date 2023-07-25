soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += c
print(f'Você informou {cont} número PARES e soma foi {soma}.')
