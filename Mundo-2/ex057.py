"""sexo = ['M', 'F']
while sexo != "M" and sexo != "F":
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Dado inválido. Por favor, informe um sexo válido [M/F]: ')).upper()
        else: """

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
idade = int(input('Quantos anos você tem? '))
print(f'Sexo {sexo}, cadastrado com sucesso!')
print(f'Sua idade é de {idade}')
