def LeiaInt(mensagem):
    '''
    Esta função recebe um valor qualquer, analiza se é ou não um valor numérico.
    Se for verdadeiro ele retorna uma menssagem informando o valor digitado.
    Se não o programa exibe uma menssagem na tela informando que o dado inserido é inválido.
    '''
    mensagem = input(f'{mensagem}')
    if mensagem.isnumeric():
        return int(mensagem)
    while True:
        print('ERRO Digite um número válido.')
        mensagem = input('Digite um número: ')
        if mensagem.isnumeric() == True:
            break
        return int(mensagem)

n = LeiaInt('Digite um número: ')
print(n)