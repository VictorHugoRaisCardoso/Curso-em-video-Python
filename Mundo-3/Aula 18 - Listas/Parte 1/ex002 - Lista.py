valores = list()
while True:
    novo_valor = int(input('Digite um valor: '))
    if novo_valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(novo_valor)
        print('Valor adicionado com sucesso!')
    sair = str(input("Quer continuar? [S/N]")).upper()
    if sair == 'N':
        valores.sort()
        break
print(f'Você digitou os valores {valores}')
