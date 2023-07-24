def NovoCadastro():
    from colorama import Fore, Back
    try:
        nome = str(input(f'{Fore.LIGHTCYAN_EX}Nome e sobrenome: ').strip().upper())
        if nome == '' or nome.isalnum():
            while nome == '' or nome.isalnum() == True:
                print('Por favor insira um nome e sobrenome válido.')
                nome = str(input('Nome e sobrenome: ').strip().upper())
        idade = int(input('Idade: '))
    except:
        while True:
            idade = str(input('ERRO. Idade inválida, tente novamente: '))
            if idade.isnumeric():
                int(idade)
                break
    finally:
        with open('FICHA.txt', 'a+') as file:
            file.write(f'{nome:<40}{idade:>15} anos\n')
        print(f'{Fore.GREEN}CADASTRO REALIZADO COM SUCESSO!')
    