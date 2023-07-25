nome = str(input('Olá prezado vendedor! Informe o nome do cliente: ')).strip().title()
####
diaria = 60.00
quilometro = 0.15
####
print('Lembre-se que o valor do aluguel é de R$60.00/dia., e o valor por Kilômetro rodado é de R$0.15!')
####
dia = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
####
total = (dia * diaria) + (km * quilometro)
####
print(f'O cliente {nome} utilizou o veiculo por {dia} dias e rodou neste período {km}Km.')
print(f'O valor total a ser pago é de R${total:.2f}! Obrigado por utilizar nossos serviços! Volte Sempre!')
