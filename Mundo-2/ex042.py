S1 = int(input('Primeiro Seguimento: '))
S2 = int(input('Segundo Seguimento: '))
S3 = int(input('Terceiro Seguimento: '))

if S1 < S2 + S3 and S2 < S3 + S1 and S3 < S2 + S1:
    print('Os seguimentos acima podem formar um triângulo ', end="")
    if S1 == S2 == S3:
        print('EQUILATERO.')
    elif S1 != S2 != S3 != S1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Estes seguimentos não podem formar um triangulo.')
