def ExibirMenuInterativo():
    from colorama import Fore, Back
    print(f'{Fore.LIGHTGREEN_EX}{"=" * 60}')
    print(f'{Fore.LIGHTBLUE_EX}{"MENU INICIAL":^60}')
    print(f'{Fore.LIGHTGREEN_EX}{"=" * 60}{Fore.RESET}')
    print(f'{Fore.CYAN}{"[ 1 ] "}{Fore.LIGHTYELLOW_EX}{"VER PESSOAS CADASTRADAS"}')
    print(f'{Fore.CYAN}{"[ 2 ] "}{Fore.LIGHTYELLOW_EX}{"NOVO CADASTRO"}')
    print(f'{Fore.CYAN}{"[ 3 ] "}{Fore.LIGHTYELLOW_EX}{"SAIR"}{Fore.RESET}')
    try:
        EscolhaDoUsuario = int(input(f'{Fore.LIGHTWHITE_EX}SUA ESCOLHA: {Fore.RESET}'))
        if EscolhaDoUsuario not in range(1, 4):
            while True:
                EscolhaDoUsuario = int(input(f'{Fore.LIGHTYELLOW_EX}Esta opção não existe, escolha apenas uma das opções disponíveis: {Fore.RESET}'))
                if EscolhaDoUsuario in range(1, 4):
                    break
    except:
        while True:
            EscolhaDoUsuario = str(input(f'{Fore.LIGHTRED_EX}ERRO! {Fore.LIGHTWHITE_EX}opção inválida, tente novamente: '))
            if EscolhaDoUsuario.isnumeric() == True:
                EscolhaDoUsuario = int(EscolhaDoUsuario)
                if EscolhaDoUsuario in range(1, 4):
                    break
    finally:
        return EscolhaDoUsuario
    