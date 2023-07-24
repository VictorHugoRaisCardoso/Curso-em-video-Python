def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Erro! preço \"{entrada}\" não é um preço válido')
        else:
            valido = True
            return float(entrada)
