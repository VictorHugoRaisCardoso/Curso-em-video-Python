import moeda

p = float(input('Digite um preço: R$ '))

print(f'O preço com um aumento de {moeda.moeda(p)} fica {moeda.moeda(moeda.aumenta(p, 10))}')
print(f'O preço com um desconto de {moeda.moeda(p)} fica {moeda.moeda(moeda.diminui(p, 13))}')
print(f'O preço dividido por {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O preço multiplicado por {moeda.moeda(p)} é {moeda.moeda(moeda.dobra(p))}')
