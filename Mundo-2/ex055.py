MAIOR = 0.0
MENOR = 0.0
for c in range(1, 6):
    PESO = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        MAIOR = PESO
        MENOR = PESO
    else:
        if PESO > MAIOR:
            MAIOR = PESO
        if PESO < MENOR:
            MENOR = PESO
print(f'O maior peso informado foi de {MAIOR}Kg!')
print(f'O menor peso informado foi de {MENOR}Kg!')
