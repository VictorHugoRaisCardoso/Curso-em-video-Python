valor_total = 0
total_de_inputs = 0

while True:
    numero_inteiro = int(input('Digite um número inteiro: '))
    if numero_inteiro == 999:
        break
    else:
        total_de_inputs += 1
        valor_total += numero_inteiro

print(f'O total de numeros digitados foi: {total_de_inputs}')
print(f'A soma de todos os valores digitados foi: {valor_total}')
