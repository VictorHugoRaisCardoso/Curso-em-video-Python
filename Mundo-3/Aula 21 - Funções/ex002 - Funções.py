def fatorial(num, show=False):
    '''
    <<< FATORIAL DE UM NÚMERO >>>
        -> num: Este parâmetro é obrigatório e deve ser um número inteiro para ser fatorado.
        -> show: Este parâmetro é opcional, se passado como True, a função vai exibir o cálculo e o resultado final.
        se não, isto é se passado como False ou não for informado a função retornará apenas o resultado final
    '''
    soma = 1
    if show == False:
        for n in range(num, 0, -1):
            soma *= n
        print(f'{soma}')
    else:
        for n in range(num, 0, -1):
            print(f'{n}', end=' ', flush=True)
            pause(0.5)
            print(f'x', end=' ', flush=True)
            pause(0.5)
            soma *= n
        print(f'= {soma}')


from time import sleep as pause

fatorial(5, show=True)
