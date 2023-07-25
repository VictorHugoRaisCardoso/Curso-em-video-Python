from funcoes import c

obj = str(input(f'{c.U()}{c.amarelo()}{c.N()}Digite Algo{c.fim()}: ')).strip()

print(f'''{c.azul()}{c.f_preto()}Está em maiúsculo{c.fim()}: {obj.isupper()}.
{c.azul()}{c.f_preto()}É numérico{c.fim()}: {obj.isnumeric()}.
{c.azul()}{c.f_preto()}Tem casas decimais{c.fim()}: {obj.isdecimal()}.
{c.azul()}{c.f_preto()}Está em minúsculo{c.fim()}: {obj.islower()}.
Tem apenas espaços: {obj.isspace()}.
É printavel: {obj.isprintable()}.
Está captalizado: {obj.istitle()}.''')
