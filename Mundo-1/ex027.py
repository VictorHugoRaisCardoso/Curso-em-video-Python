n = str(input("Digite seu nome completo: ")).strip().title()
nome = n.split()
print(f"""Seja Muito Bem Vindo {n}!
Seu primeiro nome é {nome[0]}.
Seu ultimo nome é {nome[-1]}.""")
