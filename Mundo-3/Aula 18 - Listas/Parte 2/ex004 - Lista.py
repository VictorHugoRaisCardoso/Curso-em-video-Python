matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f"Digite o numero [{l}, {c}]: "))
        matriz[l][c] = num
        if num % 2 == 0:
            pares += num
        if c == 2:
            coluna += num
        if l == 1:
            if linha == 0:
                linha = num
            else:
                if num > linha:
                    linha = num
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if c == 2:
            print()
print("-=" * 30)
print(f"A soma de todos os valores pares digitados é: {pares}")
print(f"A soma dos valores da terceiras colunas é: {coluna}")
print(f"O Maior valor da segunda linha é: {linha}")
print("-=" * 30)
