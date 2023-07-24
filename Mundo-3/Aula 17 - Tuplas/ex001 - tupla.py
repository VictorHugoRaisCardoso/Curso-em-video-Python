valor_escrito = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESEIS", "DEZESETE", "DEZEOITO", "DEZENOVE", "VINTE")

while True:
    numero = int(input("Digite um numero entre 0 e 20: "))
    if numero > 20 or numero < 0:
        print("Tente novamente. ", end="")
    else:
        print(f"Você digitou o valor {valor_escrito[numero]}")
        break
