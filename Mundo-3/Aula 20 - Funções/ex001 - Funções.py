#  Definindo a função.
def Area(largura, comprimento):
    area = largura * comprimento
    print(f'A area de um terreno de {largura} x {comprimento} é de {area}m²')


def titulo(msg):
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)


#  Programa principal.
titulo('CONTROLE DE TERRENOS')
largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))
Area(largura, comprimento)
