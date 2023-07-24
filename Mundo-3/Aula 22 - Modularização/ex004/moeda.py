def dobro(preco):
    preco = f'{preco * 2:.2f}'
    return preco


def metade(preco):
    preco = f'{preco / 2:.2f}'
    return preco


def aumento(preco, aumento):
    preco = f'{preco + (preco * aumento / 100):.2f}'
    return preco


def reducao(preco, diminuir):
    preco = f'{preco - (preco * diminuir / 100):.2f}'
    return preco


def conversor(preco):
    preco = str(preco)
    preco = preco.replace('.', ',')
    return preco


def resumo(preco, aumentar = float(), deduzir = float()):
    valor = f'{preco:.2f}'
    print(f'=' * 40)
    print(f'{"RESUMO":^40}')
    print(f'=' * 40)
    print(f'Preço analizado:            R${conversor(valor)}')
    print(f'O dobro:                    R${conversor(dobro(preco))}')
    print(f'A metade:                   R${conversor(metade(preco))}')
    print(f'Com {aumentar}% de aumento:         R${conversor(aumento(preco, aumentar))}')
    print(f'Com {deduzir}% de redução:         R${conversor(reducao(preco, deduzir))}')
    print('=' * 40)
