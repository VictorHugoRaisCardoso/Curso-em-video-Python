print(f'{"LOJA DO VITÃO":=^40}')
preco = float(input('Qual o valor da compra? R$'))
opcoes = int(input('''FORMAS DE PAGAMENTO
[ 1 ] Àvista dinheiro ou cheque
[ 2 ] Àvista no Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão
Informe a opção desejada: '''))
if opcoes == 1:
    total = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
elif opcoes == 2:
    total = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final')
elif opcoes == 3:
    total = preco / 2
    print('Sua compra será parcelada em 2x SEM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
elif opcoes == 4:
    parcelas = int(input('Quantas Parcelas? '))
    total = (preco + (preco * 20 / 100)) / parcelas
    print(f'''Sua compra será parcelada em {parcelas}x de R${total:.2f} COM JUROS
Sua compra de R${preco:.2f} vai custar {total:.2f} no final.''')
else:
    print('Opção de pagamento INVÁLIDA! TENTE NOVAMENTE!')
