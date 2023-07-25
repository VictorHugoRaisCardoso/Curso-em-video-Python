nu = int(input('Digite um número: '))
print(f'''Analizando o Número {nu}.
Unidade: {nu // 1 % 10}
Dezena: {nu // 10 % 10}
Centena: {nu // 100 % 10}
Milhar: {nu // 1000 % 10}''')