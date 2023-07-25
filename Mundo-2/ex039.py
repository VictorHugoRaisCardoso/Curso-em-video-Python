from datetime import date
from time import sleep

nome = str(input('''Seja Bem Vindo Cidadão, este é o seu simulador de alistamento.
Informe aqui a baixo o seu primeiro nome por favor.
R: ''')).strip().title()
opc = int(input('''O alistamento militar é obrigatório apenas para homens.
Por favor informe seu sexo.
[ 1 ] Digite para Homem:
[ 2 ] Digite para Mulher:
Qual é o seu sexo?: '''))

sleep(1)
if opc == 1:
    nascimento = int(input('Qual é o ano de nascimento?: '))
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    sleep(1)
    print(f'Quem nasceu em {nascimento} tem {idade} em {ano_atual}.')
    if idade < 18:
        alistamento = 18 - idade
        if alistamento == 1:
            sleep(1)
            print(f'{nome} Ainda falta {alistamento} ano para o alistamento.')
            sleep(1)
            print(f'Seu alistamento será em {ano_atual + alistamento}.')
        elif alistamento > 1:
            sleep(1)
            print(f'{nome} Ainda faltam {alistamento} anos para o alistamento.')
            sleep(1)
            print(f'Seu alistamento será em {ano_atual + alistamento}')

    elif idade > 18:
        alistamento = idade - 18
        if alistamento == 1:
            sleep(1)
            print(f'{nome} Você já deveria tem se alistado há {alistamento} ano.')
            sleep(1)
            print(f'Seu alistamento foi em {ano_atual - alistamento}.')

        elif alistamento > 1:
            sleep(1)
            print(f'{nome} Você já deveria ter se alistado há {alistamento} anos.')
            sleep(1)
            print(f'Seu alistamento foi em {ano_atual - alistamento}.')

    elif idade == 18:
        sleep(1)
        print(f'{nome} Você tem que se alistar IMEDIATAMENTE!')

elif opc == 2:
    print('Prezada cidadã, seu alistamento não é obrigatório, você está dispençada.')

print('FIM')
