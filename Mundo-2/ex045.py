from funcoes import c
from time import sleep

# Iniciar Colorido.
print(f'{c.N()}{c.f_preto()}{c.azul()}{"-=-"}{c.fim()}' * 30)
print(f'{c.N()}{c.amarelo()}{"Bem Vindo Ao JO-KEN-PÔ":^90}')
print(f'{c.N()}{c.f_preto()}{c.azul()}{"-=-"}{c.fim()}' * 30)

# Numero randomizado pela Máquina.
itens = ('PEDRA', 'PAPEL', 'TESOURA')

PC = JG = 0

for c in range(10):
    from funcoes import c
    from time import sleep
    from random import randint

    pc = randint(0, 2)
    # Escolha do Jogador.
    jogada = int(input(f'''{c.N()}{c.branco()}Você tem 3 opções:{c.fim()}
    {c.N()}{c.branco()}[ 0 ] {c.amarelo()}PEDRA{c.fim()}
    {c.N()}{c.branco()}[ 1 ] {c.magenta()}PAPEL{c.fim()}
    {c.N()}{c.branco()}[ 2 ] {c.azul()}TESOURA{c.fim()}
    {c.N()}{c.branco()}Qual é a sua escolha?{c.fim()} '''))

    # Iniciando partida.
    sleep(1)
    print(f'{c.N()}{c.vermelho()}JO{c.fim()}')
    sleep(0.8)
    print(f'{c.N()}{c.amarelo()}KEN{c.fim()}')
    sleep(0.8)
    print(f'{c.N()}{c.verde()}PÔ{c.fim()}')

    print(f'{c.N()}{c.f_preto()}{c.azul()}{"-=-" * 30}{c.fim()}')
    print(f'{c.N()}{c.branco()}{"O Computador escolheu: "}{itens[pc]}')
    print(f'{c.N()}{c.branco()}{"O Jogador escolheu: "}{itens[jogada]}')
    print(f'{c.N()}{c.f_preto()}{c.azul()}{"-=-" * 30}{c.fim()}')

    if pc == 0:
        if jogada == 0:
            sleep(1)
            print(f'{c.N()}{c.branco()}EMPATE!{c.fim()}')  # EMPATE
        elif jogada == 1:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADOR VENCEU!{c.fim()}')  # VENCEU
            JG += 1
        elif jogada == 2:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADOR PERDEU!{c.fim()}')  # PERDEU
            PC += 1
        else:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADA INVÁLIDA!{c.fim()}')  # DIGITAÇÃO INVÁLIDA

    elif pc == 1:
        if jogada == 1:
            sleep(1)
            print(f'{c.N()}{c.branco()}EMPATE!{c.fim()}')  # EMPATE
        elif jogada == 2:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADOR VENCEU!{c.fim()}')  # VENCEU
            JG += 1
        elif jogada == 0:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADOR PERDEU!{c.fim()}')  # PERDEU
            PC += 1
        else:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADA IVÁLIDA!{c.fim()}')  # DIGIAÇÃO INVÁLIDA

    elif pc == 2:
        if jogada == 2:
            sleep(1)
            print(f'{c.N()}{c.branco()}EMPATE!{c.fim()}')  # EMPATE
        elif jogada == 0:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADOR VENCEU!{c.fim()}')  # VENCEU
            JG += 1
        elif jogada == 1:
            sleep(1)
            print(f'{c.N()}{c.branco()}JOGADOR PERDEU!{c.fim()}')  # PERDEU
            PC += 1
        else:
            sleep(1)
            print(f'{c.N()}{c.branco()} JOGADA INVÁLIDA!{c.fim()}')  # DIGITAÇÃO INVÁIDA
sleep(1)
print('CALCULANDO...')
sleep(2)
if JG > PC:
    print(f'''-_-_-_-_PLACAR FINAL_-_-_-_-
JOGADOR: {JG}
COMPUTADOR: {PC}
JOGADOR VOCÊ VENCEU!''')
elif PC > JG:
    print(f'''-_-_-_-_PLACAR FINAL_-_-_-_-
JOGADOR: {JG}
COMPUTADOR: {PC}
MÁQUINA VENCEU!''')
