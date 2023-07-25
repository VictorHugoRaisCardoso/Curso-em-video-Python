from datetime import date
menor = 0
maior = 0
ano = date.today().year
for c in range(1, 8):
    idade = int(input(f'Em que ano a {c}ª pessoa Nasceu? '))
    if ano - idade >= 21:
        maior += 1
    elif ano - idade < 21:
        menor += 1
print(f'''Ao todo tivemos {maior} pessoas maiores de idade.
E tivemos {menor} pessoas menores de idade.''')
