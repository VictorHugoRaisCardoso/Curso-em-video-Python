numero = int(input('Digite um número inteiro: '))
op = int(input('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
Faça sua escolha: '''))
if op == 1:
    print(f'O valor {numero} em BINÁRIO: {numero:b}')

elif op == 2:
    print(f'O valor {numero} em OCTAL: {numero:o}')

elif op == 3:
    print(f'O valor {numero} em HEXDECIMAL: {numero:x}')

else:
    print('Opção inválida. Tente novamente.')
