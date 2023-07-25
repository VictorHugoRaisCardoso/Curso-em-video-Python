valor_disponivel = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = float(input('Informe o valor atual do Dolar: $'))
euro = float(input('Informe o valor atual do Euro: ¢'))
c_dolar = valor_disponivel / dolar
c_euro = valor_disponivel / euro
print(f'Baseado nas informações disponíbilizadas, hoje com o valor de R${valor_disponivel:.2f} '
      f'é possível comprar ${c_dolar:.2f} ou ¢{c_euro:.2f}.')
