from time import sleep

# Memorizando o valor da casa.
imovel = float(input('Qual é o valor total do imóvel a ser financiado?: R$'))
sleep(1)
# Memorizando o valor da renda.
salario = float(input('Qual é o valor liquido da sua renda?: R$'))
sleep(1)
# Dando escolhas para variar a simulação.
alternativa = int(input('''Escolha o critério de tempo de financiamento.
Digite (1) para mês:
Digite (2) para ano:
R: '''))
sleep(1)
# Montando a estrutura da primeira alternativa.
if alternativa == 1:
    # Perguntando ao usuário a quantidade de parcelas a ser financiada.
    mes = int(input('Em quantas vezes será financiado o valor total do imóvel?: '))
    sleep(1)
    # Calculando valores do financiamento.
    parcelas = imovel / mes
    # Cálculo de verificação excedente de 30% da renda.
    limite = salario * 30 / 100
    # Condicionando os valores.
    if parcelas > limite:
        # Recusando Financiamento.
        sleep(1)
        print(f'O valor da parcela é de R${parcelas:.2f}, este valor compromete mais de '
              f'30% do seu salário que seria de R${limite}.')
        sleep(1)
        print('Devido a este fator, lamentamos informar que seu financiamento não pode ser'
              'aprovado! Aumente sua receita ou financie uma casa de menor valor!')
    # Condicionando os valores.
    elif parcelas <= limite:
        sleep(1)
        # Aprovando Financiamento.
        print('MEUS PARABÉNS SEU FINANCIAMENTO PODE SER APROVADO!')
        sleep(1)
        # Criando variável de finalização.
        final = int(input('''Para validar o financiamento digite (1):
Para finalizar sua simulação digite (2):
R: '''))
        sleep(1)
        # Encaminhando Financiamento.
        if final == 1:
            print('Estamos encaminhando sua simulação para um vendedor, em breve ele entrará em contato.')
            sleep(1)
            print('Obrigado pela preferência!')
        # Finalizando Simulação.
        elif final == 2:
            print('Lamentamos não poder fechar negócio com você agora, esperamos te ver em breve, até mais.')

# Montando a estrutura da segunda alternativa.
elif alternativa == 2:
    # Criando uma variavel para o tempo de financiamento.
    sleep(1)
    ano = int(input('De quantos anos será o financiamento do imóvel?: '))
    # Calculado parcelas do imovel.
    parcelas = imovel / (ano * 12)
    # Calculando limite de 30% da renda.
    limite = salario * 30 / 100

    # Criando condições de financiamento.
    if parcelas > limite:
        # Recusando Financiamento.
        sleep(1)
        print(f'O valor da parcela é de R${parcelas:.2f}, este valor compromete mais de '
              f'30% do seu salário que seria de R${limite}.')
        sleep(1)
        print('Devido a este fator, lamentamos informar que seu financiamento não pode ser'
              'aprovado! Aumente sua receita ou financie uma casa de menor valor!')

    # Condicionando os valores.
    elif parcelas <= limite:
        sleep(1)
        # Aprovando Financiamento.
        print('MEUS PARABÉNS SEU FINANCIAMENTO PODE SER APROVADO!')
        sleep(1)
        # Criando variável de finalização.
        final = int(input('''Para validar o financiamento digite (1):
Para finalizar sua simulação digite (2):
R: '''))
        sleep(1)
        # Encaminhando Financiamento.
        if final == 1:
            print('Estamos encaminhando sua simulação para um vendedor, em breve ele entrará em contato.')
            sleep(1)
            print('Obrigado pela preferência!')
        # Finalizando Simulação.
        elif final == 2:
            sleep(1)
            print('Lamentamos não poder fechar negócio com você agora, esperamos te ver em breve, até mais.')

sleep(1)
print('Fim da Simulação...')
