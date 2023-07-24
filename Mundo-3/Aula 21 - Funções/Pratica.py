cor = (
    '\033[m',           #  0 - Limpa
    '\033[0;30,41m',    #  1 - Vermelho
    '\033[0;30;42m',    #  2 - verde
    '\033[0;30;43m',    #  3 - Amarelo
    '\033[0;30;44m',    #  4 - Azul
    '\033[0;30;45m',    #  5 - Roxo
    '\033[47m'          #  6 - Branco
    )

'''
Financiamento Bancário.
O Programa vai receber várias informações, são elas:
    - Nome.
    - Renda média mensal.
    - Reserva financeira.
    - Score.
    - Valor do impréstimo
Após a as infromações serem passadas o simulador deve
avaliar se o valor solicitado pode ou não ser emprestado.
Se não for possível o programa deverá apresentar um 
empréstimo que caiba dentro do orçamento da pessoa
'''
def decor(texto, c=0, borda=False):
    if borda:
        print(f'{cor[c]}{"=" * (len(texto)+4)}')
        print(f'{cor[c]}  {texto}')
        print(f'{cor[c]}{"=" * (len(texto)+4)}{cor[0]}')
    else:
        print(f'{cor[c]}{texto}', end='')
        print(cor[0])


def menu():
    global cliente
    decor(cliente['Nome'], 4)
    
def Simulador(nome, rmm, rf, vi):
    pass

#  Programa pricipal
cliente = {
    'Nome': '',
    
}
menu()
