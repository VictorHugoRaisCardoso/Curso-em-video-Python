def sorteia(lista):
    for i in range(0, 5):
        lista.append(ri(0, 20))
    print(f'Os numeros sorteados foram {lista}')
        

def somaPar(lista):
    n = 0
    for i in lista:
        if i % 2 == 0:
            n += i
    print(f'A soma entre todos os numeros pares é {n}')
    
    
#  Programa principal
from random import randint as ri
numeros = []
sorteia(numeros)
somaPar(numeros)
