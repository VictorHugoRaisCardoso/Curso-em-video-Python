from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
print('Sou seu computador...')
computador = randint(0, 10)
print('''Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
palpite = int(input('Qual é o seu palpite?: '))
tentativas = 1
while palpite != computador:
    if palpite < computador:
        palpite = int(input('Mais... Tente mais uma vez: '))
    elif palpite > computador:
        palpite = int(input('Menos... Tente mais uma vez: '))
    tentativas += 1
print(f'Você acertou com {tentativas} tentativas. Parabéns!')
