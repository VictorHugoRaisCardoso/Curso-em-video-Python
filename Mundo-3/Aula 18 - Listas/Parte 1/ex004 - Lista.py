lista = list()

while True:
    novo_valor = int(input("Digite um valor: "))
    lista.append(novo_valor)
    print(f"O numero {novo_valor} foi adicionado com sucesso!")
    sair = str(input("Quer continuar? [S/N] ")).upper()
    if sair in 'N':
        break
print("=" * 30)
print(f"Você digitou um total de {len(lista)} numeros.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}")
num = 0
for i in range(0, len(lista)):
    if lista[i] == 5:
        num = lista[i]
if num == 5:
    print("O numero 5 faz parte da lista!")
else:
    print("O numero 5 não faz parte da lista!")
