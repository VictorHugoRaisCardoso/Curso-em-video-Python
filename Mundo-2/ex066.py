valorTotal = 0
totalDeInputs = 0

while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    else:
        totalDeInputs += 1
        valorTotal += num

print(f'O total de numeros digitados foi: {totalDeInputs}')
print(f'A soma de todos os valores digitados foi: {valorTotal}')
