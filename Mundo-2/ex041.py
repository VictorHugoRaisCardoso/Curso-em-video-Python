from datetime import date

hoje = date.today().year
nascimento = int(input('Ano do Nascimento: '))
idade = hoje - nascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JÚNIOR.')
elif idade <= 25:
    print('Categoria: SÊNIOR.')
elif idade > 25:
    print('Categoria: MASTER.')
