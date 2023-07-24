def titulo(num):
    print('=' * 30)
    print(f'      {num}      ')
    print('=' * 30)


def soma(a, b):
    s = a + b
    print(f'A soma ente {a} + {b} = {s}')
    
    
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(lista)


valores = [2, 6, 4, 3, 5]
titulo('SOMA DE VALORES')
soma(7, 3)
titulo('DOBRANDO VALORES')
dobra(valores)
