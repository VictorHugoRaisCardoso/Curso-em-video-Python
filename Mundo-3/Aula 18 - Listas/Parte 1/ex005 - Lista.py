lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    sair = str(input("Quer continuar? [S/N]")).upper()
    if sair in "N":
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print('=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')
