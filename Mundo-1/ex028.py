from random import randint

numero = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))

if jogador == numero:
    print(f"A máquina escolheu o numero {numero}, VOCÊ VENCEU!!!")
    print('______________________VENCEDOR!______________________')

else:
    print(f'A máquina escolheu o número {numero}, VOCÊ PERDEU!!!')
    print('______________________PERDEDOR!______________________')
