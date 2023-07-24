teste = str(input('Digite a expressão: '))
pd = teste.count('(')
pe = teste.count(')')
if pd == pe:
    print('Sua expressão é válida')
else:
    print('Sua expressão está incorreta')
