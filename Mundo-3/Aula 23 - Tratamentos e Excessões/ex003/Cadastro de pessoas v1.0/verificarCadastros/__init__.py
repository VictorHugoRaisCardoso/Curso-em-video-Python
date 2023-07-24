def VerCadastros():
    from colorama import Fore, Back
    from time import sleep
    with open('FICHA.txt', 'r') as file:
        print(f'{Fore.LIGHTGREEN_EX}{"=" * 60}')
        for pessoa in file:
            print(f'{Fore.LIGHTWHITE_EX}{pessoa}{Fore.RESET}', end='')
            sleep(1)
