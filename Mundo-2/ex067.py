from time import sleep

while True:
    tabuada = int(input('Informe um valor negativo para interromper\nA tabuada de que numero você gostaria de ver agora? '))
    if tabuada < 0:
        break
    else:
        for numero in range(0, 11):
            sleep(1)
            print(f'{numero:>2} x {tabuada:>2} = {tabuada * numero:>2}')
