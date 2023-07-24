from ferramentas.Interface import linha, LeiaInt
from time import sleep


def Cadastar():
    linha()
    nome = str(input("Nome: ").upper())
    idade = LeiaInt("Idade: ")
    with open('Ficha.txt', 'a+') as file:
        file.write(f'{nome:<40}{idade:>15} anos\n')


def VerCadastro():
    with open('Ficha.txt', 'r+') as file:
        linha()
        for i in file:
            print(i, end='')
            sleep(1)

def SeArquivoNaoExistir():
    try:
        with open('Ficha.txt', 'rt') as file:
            file.read()
    except FileNotFoundError:
        with open('Ficha.txt', 'a+') as file:
            file.close()
            print('Arquivo "Ficha.txt" criado com sucesso!')