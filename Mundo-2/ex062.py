def desing():
    a = print('=' * 40)
    return a

desing()
print(f'{"MOSTRANDO OS TERMOS DE UMA P.A.": ^40}')
desing()

termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo = termo
contador = 1
termo_total = 0
mais = 10
while mais != 0:
    termo_total += mais
    while contador <= termo_total:
        print(f'{termo} => ', end='')
        contador += 1
        termo += razao
    print(f'PAUSA ')

    mais = int(input("Quantos termos a mais você quer mostrar? "))
print(f'Progressão finalizada com {termo_total} termos mostrados.')
