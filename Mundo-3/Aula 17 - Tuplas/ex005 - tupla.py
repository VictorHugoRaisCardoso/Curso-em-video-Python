lista = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.00,
         "Estojo", 25.00,
         "Transferidor", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Canetas", 22.30,
         "Livro", 34.90)
print("=" * 80)
print(f"{'LISTAGEM DE PREÇO':^80}")
print("=" * 80)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<70}", end="R$")
    else:
        print(f"{lista[i]:>8.2f}")
print("=" * 80)
