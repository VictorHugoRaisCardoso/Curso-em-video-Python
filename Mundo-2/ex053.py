frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo')
