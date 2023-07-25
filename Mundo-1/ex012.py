clinte = str(input('Seja bem vindo prezado cliente, como posso te chamar? '))
print(f'Prazer em te conhecer {clinte}! Fique a vontade para consultar os preços e descontos!')
valor_produto = float(input('Qual é o preço do produto? R$'))
valor_desconto = float(input('Qual é o valor do desconto? '))
preco_final = valor_produto - (valor_produto * valor_desconto / 100)
print(f'{clinte}, o produto que custava R${valor_produto:.2f}, '
      f'na promoção com desconto de {valor_desconto:.0f}% vai custar R${preco_final:.2f}')