from random import randint
from time import sleep

vitoriasConsecutivas = int()

print("=" * 60)
print(f'{"Vamos Jogar Par ou Impar":^60}')
print("=" * 60)

while True:
    resultado = 0
    computador = randint(0,100)
    numeroDoJogador = int(input('Digite um número: '))
    escolhaJogador = str(input("Par ou Impar [P/I]: ")).upper()
    resultado = computador + numeroDoJogador
    
    if (escolhaJogador in 'P' or escolhaJogador in 'I'):
        if (resultado % 2 == 0 and escolhaJogador == 'P' or resultado % 2 != 0 and escolhaJogador == 'I'):
            print(f'Você jogou {numeroDoJogador} e o computador {computador}. Total de {resultado} DEU PAR')
            print(f'Você venceu!')
            vitoriasConsecutivas += 1
        else:
            print(f'Você perdeu.')
            break
print(f'Você venceu por {vitoriasConsecutivas} vezes consecutivas.')
