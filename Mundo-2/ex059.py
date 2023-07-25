from time import sleep
valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))
sair = 0
while sair != 5:
    opcao = int(input('''-=-=-=-=-=-MENU INICIAL-=-=-=-=-=-
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR VALOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA 
>>>>> QUAL É A SUA OPÇÃO? '''))
    if opcao == 1:
        total = valor_1 + valor_2
        sleep(1)
        print(f'A soma entre {valor_1} e {valor_2} é igual a {total}')
    elif opcao == 2:
        total = valor_1 * valor_2
        sleep(1)
        print(f'O resultado de {valor_1} x {valor_2} é {total}')
    elif opcao == 3:
        if valor_1 > valor_2:
            maior = valor_1
            sleep(1)
            print(f'O maior valor é {maior}')
        elif valor_1 < valor_2:
            maior = valor_2
            sleep(1)
            print(f'O maior valor é {maior}')
        else:
            sleep(1)
            print('Os dois número informados são iguais!')
    elif opcao == 4:
        print('Informe os novos números.')
        sleep(1)
        valor_1 = int(input('Primeiro valor: '))
        sleep(1)
        valor_2 = int(input('Segundo valor: '))
    elif opcao == 5:
        sair = 5
        print('Finalizando...')
        sleep(5)
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
print('Fim do Programa. Volte sempre!')
