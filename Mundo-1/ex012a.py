nome = str(input('Seja bem vindo prezado cliente, como posso te chamar? ')).strip().title()
print(f'Prazer em te conhecer {nome}! Fique a vontade, faça sua consulta de preço!')
produto = float(input('Informe o valor do produto: R$'))
avista = produto - (produto * 15 / 100)
prazo = produto + (produto * 30 / 100)
print(f'''O produto que custa R${produto:.2f}, se pago avista tem 15% de desconto, sairá por apenas R${avista:.2f}
Se pago parcelado, terá um acrécimo de 30% no valor do produto, seu preço final será de R${prazo:.2f}.''')
