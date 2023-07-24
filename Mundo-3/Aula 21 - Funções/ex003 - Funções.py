def ficha(nome=str, gols=0):
    '''
<<< FICHA >>>
Esta função recebe apenas dois parâmetros opcionais, são eles:
    -> nome: Recebe uma String opcional, se nada for informado ela retorna "<<< Desconhecido >>>".
    -> gols: Recebe uma String opcional, se nada for informado ou o valor informado for diferente de um valor
passivo de conversão numérica gols é convertido um valor Interio igual a 0.
'''
    if gols.isnumeric() == True:
        gols = int(gols)
    else:
        gols = 0
    if nome == '':
        nome = '<<< Desconhecido >>>'
    print(f'O jogador {nome} fez {gols} gols')
    


nome = str(input('Nome do jogador: '))
gols = str(input('Gols: '))

ficha(nome, gols)
