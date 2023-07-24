numeros = (int(input("Digite um valor: ")), int(input("Digite o segundo valor: ")), int(input("Digite o terceiro valor: ")), int(input("Digite o quarto valor: ")))
print(f"Você digitou os valores: {numeros}")
print(f"O valor 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O numero 3 apareceu na {numeros.index(3) + 1}º posição")
else:
    print("O numero 3 não apareceu em nenhuma posição")
print("Os numeros pares digitados foram: ", end="") 
for i in numeros:
    if i % 2 == 0:
        print(f"{i}", end=" ")

