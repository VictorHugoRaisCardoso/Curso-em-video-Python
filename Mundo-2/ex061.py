from os import system

def cls():
    a = system("cls")
    return a


def desing():
    a = print('=' * 40)
    return a

desing()
print(f'{"10 TERMOS DE UMA P.A.": ^40}')
desing()

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo
contador = 1
while contador <= 10:
     print(f'{decimo} x ', end='')
     contador += 1
     decimo += razao
print('Fim')
