salario = float(input('Informe o salário do funcionário: R$'))
'''if salario > 1250.00:
    print(f'O salário atual é de R${salario:.2f} com 10% de aumento passa a ser R${salario + (salario * 10 / 100):.2f}')
if salario <= 1250.00:
    print(f'O salário atual é de R${salario:.2f} com 15% de aumento passa a ser R${salario + (salario * 15 / 100):.2f}')'''
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f}.')
