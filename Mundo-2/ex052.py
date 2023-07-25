from funcoes import c
numero = int(input(f'{c.branco()}Digite um número: '))
total = 0
for count in range(1, numero + 1):
    if numero % count == 0:
        print(f'{c.amarelo()}', count, end=' ')
        total += 1
    else:
        print(f'{c.vermelho()}', count, end=' ')
if total > 2:
    print(f'\n{c.branco()}O número {c.azul()}{numero} {c.branco()}foi divisível {c.amarelo()}{total} {c.branco()}vezes.')
    print(f'Por isto ele {c.vermelho()}NÃO {c.branco()}é um {c.amarelo()}NÚMERO PRIMO.')
elif total == 2:
    print(f'\n{c.branco()}O número {c.azul()}{numero} {c.branco()}foi divisível {c.amarelo()}{total} {c.branco()}vezes.')
    print(f'Por isto ele {c.azul()}É {c.branco()}UM {c.azul()}NÚMERO {c.amarelo()}PRIMO')
