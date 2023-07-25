def linha():
    a = print('='* 40)
    return a


linha()
print(f'{"Sequência de Fibonacci": ^40}')
linha()

valor = int(input("Quantos termos você quer mostrar?: "))
termo_1 = 0
termo_2 = 1
clock = 3
linha()
print(f'{termo_1} -> {termo_2} -> ', end='')
while clock <= valor:
    termo_3 = termo_1 + termo_2
    print(f'{termo_3} -> ', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    clock += 1
print('FIM')
linha()
