"""Precisamos saber quantos numeros foram digitados. Qual a média
entre eles. Informe também qual é o maior e o menor número entre eles"""
resposta = "S"
total = maior = menor = media = soma = 0
while "S" in resposta:
    numero = int(input('Digite um número: '))
    total += 1
    soma += numero
    if total == 1:
        maior = menor = numero
    else:
        if maior < numero:
            maior = numero
        if maior > numero:
            menor = numero
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / total
print(f'''Você digitou {total} numeros, a média entre eles é {media:.0f}.
O maior numero digitado foi {maior} e o menor foi {menor}.''')
