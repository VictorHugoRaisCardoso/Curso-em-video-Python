from colorama import Fore

def LeiaInt(mensagem):
    try:
        mensagem = int(input(mensagem))
        return mensagem
    
    except KeyboardInterrupt:
        mensagem = 0
        return f'O usuário preferiu não informar o valor. Valor definido como {mensagem}'
    
    except (TypeError, ValueError):
        while True:
            mensagem = str(input(f'ERRO: Isto não é um número!\nDigite apenas um valor interiro: '))
            if mensagem.isnumeric():
                int(mensagem)
                return mensagem
                break
    

def linha(tamanho = 60):
    print('=' * tamanho)


def Cabecalho(texto):
    linha()
    print(f'{texto.center(60)}')
    linha()
    

def menu(lista):
    Cabecalho("MENU INICIAL")
    contador = 1
    for opcao in lista:
        print(f'{Fore.BLUE}[{contador}]{Fore.YELLOW} - {opcao}{Fore.RESET}')
        contador += 1
    escolha = LeiaInt("Sua opção: ")
    return escolha
