peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f} e ', end="")
if imc < 18.5:
    print('você está ABAIXO DO PESO. FIQUE ALERTA!')
elif 18.5 <= imc < 25:
    print('você está no PESO IDEAL!')
elif 25 <= imc <= 30:
    print('você está ACIMA DO PESO!')
elif 30 <= imc <= 40:
    print('você está com OBESIDADE!')
elif imc > 40:
    print('você está com OBESIDADE MORBIDA!')