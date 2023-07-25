# ANALISADOR GERAL.
# VARIAVEIS NECESSÁRIAS.
mulher_jovem = 0
homem_velho = ''
homem_idade = 0
idade_total = 0
# LAÇO DE REPETIÇÃO.
for p in range(1, 5):
    # COLETANDO DADOS DE CADA PESSOA.
    print(f'----- {p}ª pessoa -----')
    nome = str(input('Nome: ').title().strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    # SOMANDO IDADE NA VARIAVEL "IDADE_TOTAL".
    idade_total += idade
    # CODIÇÃO DE ATRIBUIÇÃO DE VARIAVEIS PARA CÁLCULO.
    # CONDIÇÃO PARA HOMENS.
    if sexo == 'M':
        if idade > homem_idade:
            homem_idade = idade
            homem_velho = nome
    # CONDIÇÃO PARA MULHERES.
    else:
        if sexo == 'F':
            if idade < 20:
                mulher_jovem += 1
# VARIAVEL DE MEDIA ENTRE AS IDADES.
media = idade_total / 4
# ESCREVENDO NA TELA O RESULTADO DOS DADOS COLETADOS.
print(f'''A idade média foi de {media} anos.
O Homem mais velho tem {homem_idade} anos e ele se chama {homem_velho}.
Tivemos no total {mulher_jovem} mulheres com idade menor que 20 anos.''')
