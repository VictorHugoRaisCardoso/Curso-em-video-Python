nome = str(input('Qual é o seu nome? '))
celsius = float(input(f'{nome}, digite um valor em °C: '))
fahrenhite = (celsius * 1.8) + 32
print(f'{nome}, a temperatura de {celsius:.1f}°C corresponde a {fahrenhite:.1f}°F!')
