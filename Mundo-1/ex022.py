from time import sleep
nome = str(input('Digite seu nome COMPLETO: ')).strip()
ltrs = len(nome) - nome.count(' ')
n1 = nome.split()
sleep(3)
print(f'''Analizamos seu nome, logo a baixo temos um breve relatório sobre ele.
Seu nome em Maiúsculas fica: {nome.upper()}.
Em Minúsculas fica: {nome.lower()}.
Seu nome ao todo contém {ltrs} letras.
Seu primeiro nome é {n1[0]} e ele contém {len(n1[0])}''')
