import moeda

p = float(input('Digite um preço: R$'))

print(f'O preço com 10% de aumento é {moeda.aumenta(p, 10, True)}')
print(f'O preço com 13% de desconto é {moeda.diminui(p, 13, True)}')
print(f'O preço multiplicado por 2 é {moeda.dobra(p, True)}')
print(f'O preco dividido por 2 é {moeda.divide(p, True)}')
