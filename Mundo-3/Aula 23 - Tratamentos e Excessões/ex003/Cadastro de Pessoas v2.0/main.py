from ferramentas.Interface import *
from ferramentas.Cadastro import *
from time import sleep


SeArquivoNaoExistir()

while True:
    opção = menu(["VER PESSOAS CADASTRADAS", "NOVO CADASTRO", "SAIR DO SISTEMA"])
    if opção == 1:
        VerCadastro()
    elif opção == 2:
        Cadastar()
    else:
        Cabecalho(f'{Fore.LIGHTYELLOW_EX}SAINDO DO SISTEMA... {Fore.LIGHTWHITE_EX}ATÉ LOGO!')
        break
    sleep(2)
