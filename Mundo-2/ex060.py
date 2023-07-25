"""from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
print(f'{factorial(numero)}')"""

NUMERO = int(input('DIGITE UM NÚMERO: '))
CONTADOR = NUMERO
FATORIAL = NUMERO
print(f'CALCULANDO {NUMERO}!: ', end='')
print(f'{NUMERO} ', end='')
while CONTADOR > 1:
    print(f'x ', end='')
    CONTADOR -= 1
    FATORIAL *= CONTADOR
    print(f'{CONTADOR} ', end='')
print(f'= {FATORIAL}')
