import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobra(p):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumenta(p, 10):.2f}')
print(f'Diminuindo 13%, temos R${moeda.diminui(p, 13):.2f}')
