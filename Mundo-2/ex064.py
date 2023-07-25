numero = soma = clock = 0
while numero != 999:
    numero = int(input('Digite um número [999 para Parar]: '))
    if numero != 999:
        soma += numero
        clock += 1
print(f'Você digitou {clock} numeros, e a soma entre eles foi {soma}')
