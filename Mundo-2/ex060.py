"""from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
print(f'{factorial(numero)}')"""

numero = int(input('DIGITE UM NÚMERO: '))
contador = numero
fatorial = numero
print(f'CALCULANDO {numero}!: ', end='')
print(f'{numero} ', end='')
while contador > 1:
    print(f'x ', end='')
    contador -= 1
    fatorial *= contador
    print(f'{contador} ', end='')
print(f'= {fatorial}')
