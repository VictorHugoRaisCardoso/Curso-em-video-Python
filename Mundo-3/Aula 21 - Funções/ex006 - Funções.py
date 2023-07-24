cor = (
    '\033[m',           #  0 - Limpa
    '\033[0;30,41m',    #  1 - Vermelho
    '\033[0;30;42m',    #  2 - verde
    '\033[0;30;43m',    #  3 - Amarelo
    '\033[0;30;44m',    #  4 - Azul
    '\033[0;30;45m',    #  5 - Roxo
    '\033[47m'          #  6 - Branco
    )

def decor(texto, c=0, abas=False):
    if abas:
        print(f'{cor[c]}', end='')
        print('=' * len(texto))
        print(texto)
        print(f"{'=' * len(texto)}{cor[0]}")
    else:
        print(f'{cor[c]}{texto}{cor[0]}')
        
    
def PyHelp():
    '''
<<< PyHelp>>>
    Ao iniciar o programa o usuário pode informar o nome de um comando ou biblioteca que deseja conhecer mais.
    O programa exibe na tela o resultado da pesquisa.
    Para finalizar o programa basta digitar a palavra FIM não importando se minúscula, maiúscula ou capalizada.
    '''
    decor('  SISTEMA DE AJUDA PYHELP  ', 4, True)
    sleep(0.5)
    while True:
        comando = str(input(f'{cor[6]}Comando ou Biblioteca -->{cor[0]} '))
        if comando.upper() == "FIM":
            decor('VOLTE SEMPRE!')
            break
        decor('Buscando informações... ', 2, True)
        decor(help(comando), 6)


from time import sleep        
PyHelp()
