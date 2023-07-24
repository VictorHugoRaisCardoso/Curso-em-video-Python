#  Utilizando o help(Objeto) pode ter acesso as informações sobre as funcionalidades do Python
from time import sleep
def contador(i, f, p):
    '''
    i = O parametro i corresponde ao início da contagem
    f = O parametro f corresponde ao Fim da contagem
    p = O parametro p corresponde ao passo da contagem
    return: Não tem retorno
    '''
    while i < (f + 1):
        print(f'{i} ', end='', flush=True)
        i += p
        sleep(0.5)
    print('FIM!')


#  Parametros opicionais
def somar(x=0, b=0, c=0):
    '''
    a = Corresponde ao primeiro valor
    b = Corresponde ao segundo valor
    c = Corresponde ao terceiro valor
    Caso nenhum parametro seja informado o valor será 0.
    '''
    s = x + b + c
    print(f'A soma vale {s}')



#  Escopo de Variavel
def teste(b):
    '''
    variaveis criadas dentro de funções ou objetos são variaveis locais, nao podem ser chamadas no escopo global
    variaveis criadas fora de funções ou objetos são variaveis de escopo global, podem ser usadas dentro e fora de funções e etc
    Em python se duas variaveis com o mesmo nome estiverem em escopos diferentes elas serão variaveis diferentes
    Para usar uma variavel global dentro de um escopo local é necessário declarar explicitamente que quer utilizar a variavel global
    A forma de fazer isto é chamando dentro da função "global" e o nome da variavel que deseja utilizar.
    '''
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#  Retorno de Valores
'''
As funções com retorno podem ser armazendas em variaveis para serem usadas posteriomente
'''
