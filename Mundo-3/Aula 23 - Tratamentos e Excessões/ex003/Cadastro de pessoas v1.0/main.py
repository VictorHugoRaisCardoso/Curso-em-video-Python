from verificarCadastros import VerCadastros
from cadastramento import NovoCadastro
from menu import ExibirMenuInterativo
from colorama import Fore, Back
from time import sleep

while True:
    escolha = ExibirMenuInterativo()
    if escolha == 1:
        print(f'{Fore.LIGHTGREEN_EX}=' * 60)
        print(f'{Fore.LIGHTWHITE_EX}{"Opção 1":^60}{Fore.RESET}')
        VerCadastros()
    elif escolha == 2:
        print(f'{Fore.LIGHTGREEN_EX}=' * 60)
        print(f'{Fore.LIGHTWHITE_EX}{"Opção 2":^60}{Fore.RESET}')
        NovoCadastro()
        sleep(1.5)
    else:
        print(f'{Fore.LIGHTGREEN_EX}=' * 60)
        print(f'{Fore.LIGHTWHITE_EX}{"Opção 3":^60}{Fore.RESET}')
        print(f'{Fore.LIGHTYELLOW_EX}SCRIPT FINALIZADO. VOLTE SEMPRE!{Fore.RESET}')
        sleep(3)
        break
