def desing():
    a = print('=' * 40)
    return a

desing()
print(f'{"10 TERMOS DE UMA P.A.": ^40}')
desing()

primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(f'{c} ->', end=" ")
print('ACABOU')
