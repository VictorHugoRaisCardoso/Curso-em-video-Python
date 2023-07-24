from time import sleep as calma

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1 
    print('=' * 60)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')

    if inicio < fim:
        while inicio < (fim + 1):
            print(f'{inicio}', end=' ', flush=True)
            calma(0.5)
            inicio += passo

    elif inicio > fim:
        while inicio > (fim - 1):
            print(f'{inicio}', end=' ', flush=True)
            calma(0.5)
            inicio -= passo
    print("FIM!")
    

contador(0, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
