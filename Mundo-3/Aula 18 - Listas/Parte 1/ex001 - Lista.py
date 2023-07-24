valores = [] # Cria lista para armazenar os valores
maior = menor = int() # Cria duas variaveis para armazenar o maior e menor valor
for i in range(0, 5): # Cria um laço para ler valores 
    valores.append(int(input(f'Digite um valor na posição {i}: '))) # Le a entrada e adiciona o valor na lista
for pos, valor in enumerate(valores): # Percorre toda a lista para verificar qual foi o maior e menor valor
    if pos == 0: # Se a posição for igual a 0
        maior = menor = valor
    else: # Se não for igual a 0
        if valor < menor: # Testa se o valor dentro da variavel valor é menor que a variavel menor
            menor = valor
        if valor > maior: # Testa se o valor dentro da variavel valor é maior que a variavel maior 
            maior = valor
print('=' * 40)
print(f'Você digitou os valores {valores}') # Exibe os valores dentro da lista valores
print(f'O maior valor digitado foi {maior} nas posições ', end='') # Mostra em que posição foi digitado o maior valor e qual valor
for pos in range(0, len(valores)):
    if maior == valores[pos]:
        print(pos, end='... ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos in range(0, len(valores)):
    if menor == valores[pos]:
        print(pos, end='... ')
