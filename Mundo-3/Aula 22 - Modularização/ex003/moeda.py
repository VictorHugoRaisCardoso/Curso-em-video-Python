def aumenta(preco, aumento, convert = False):
    preco = f'{(preco + ((preco * aumento) / 100)):.2f}'
    if convert:
        preco = str(preco)
        preco = preco.replace('.', ',')
        return f'R${preco}'
    else:
        return preco


def diminui(preco, diminuir, convert = False):
    preco = f'{(preco - ((preco * diminuir) / 100)):.2f}'
    if convert:
        preco = str(preco)
        preco = preco.replace('.', ',')
        return f'R${preco}'
    else:
        return preco


def divide(preco, convert = False):
    preco = f'{preco / 2:.2f}'
    if convert:
        preco = str(preco)
        preco = preco.replace('.', ',')
        return f'R${preco}'
    else:
        return preco


def dobra(preco, convert = False):
    preco = f'{preco * 2:.2f}'
    if convert:
        preco = str(preco)
        preco = preco.replace('.', ',')
        return f'R${preco}'
    else:
        return preco
    
