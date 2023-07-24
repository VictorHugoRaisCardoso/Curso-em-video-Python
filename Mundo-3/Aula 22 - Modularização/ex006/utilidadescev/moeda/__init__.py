def dobro(preco):
    preco = preco * 2
    return preco


def metade(preco):
    preco = preco / 2
    return preco


def aumento(preco, aumento = 0):
    preco = preco + (preco * aumento / 100)
    return preco


def reducao(preco, diminuir = 0):
    preco = preco - (preco * diminuir / 100)
    return preco


def conversor(preco):
    preco = str(preco)
    preco = preco.replace('.', ',')
    return preco


def resumo(preco, aumentar = 0, deduzir = 0):
    valor = float(preco)
    print(f'=' * 40)
    print(f'{"RESUMO":^40}')
    print(f'=' * 40)
    print(f'Preço analizado:            R${conversor(valor)}')
    print(f'O dobro:                    R${conversor(dobro(preco))}')
    print(f'A metade:                   R${conversor(metade(preco))}')
    print(f'Com {aumentar}% de aumento:         R${conversor(aumento(preco, aumentar))}')
    print(f'Com {deduzir}% de redução:         R${conversor(reducao(preco, deduzir))}')
    print('=' * 40)
