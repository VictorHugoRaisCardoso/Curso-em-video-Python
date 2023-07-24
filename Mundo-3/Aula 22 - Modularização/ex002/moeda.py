def aumenta(numero=0, percent=0):
    """
    Função aumenta iniciamente recebe dois parâmetros OBRIGATÓRIOS, são eles:
        - numero: Dentro deste parâmetro deve conter um valor inteiro (int) ou valor flutuante (float).
        - percent: Dentro deste parâmetro deve conter um valor inteiro (int) ou valor flutuante (float), este
        valor corresponte a porcentagem que será adicionada ao parâmetro numero, depois de calculado o valor
        será armazenado em uma variavel chamada valor que retorna novo valor com o calculo já feito.
    """
    valor = numero + ((numero * percent) / 100)
    return valor


def diminui(numero=0, percent=0):
    """
    Função diminui iniciamente recebe dois parâmetros OBRIGATÓRIOS, são eles:
        - numero: Dentro deste parâmetro deve conter um valor inteiro (int) ou valor flutuante (float).
        - percent: Dentro deste parâmetro deve conter um valor inteiro (int) ou valor flutuante (float), este
        valor corresponte a porcentagem que será subtraido do parâmetro numero, depois de calculado o valor
        será armazenado em uma variavel chamada valor que retorna novo valor com o calculo já feito.
    """
    valor = numero - ((numero * percent) / 100)
    return valor
    
    
def dobra(numero=0):
    """
    A função dobra recebe um único parâmetro e este parâmetro é armazenado em uma variavel chamada valor já
    multiplicado por 2, depois retorna o resultado dentro de valor.
    """
    valor = numero * 2
    return valor


def metade(numero=0):
    """
    A função metade recebe um único parâmetro e este parâmetro é armazenado em uma variavel chamada valor já
    dividido por 2, depois retorna o resultado dentro de valor.
    """
    valor = numero / 2
    return valor


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')
