palavras = ("abacate", "abacaxi", "melao", "melancia")
for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} tem as vogais: ", end=" ")
    for letra in palavra:
        if letra in "aeiou":
            print(f"{letra}", end=" ")
