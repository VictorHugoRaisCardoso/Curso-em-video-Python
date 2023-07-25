from funcoes import c

numero = int(input(f'{c.N()}{c.verde()}Digite um número{c.fim()}: '))
dob = numero * 2
tri = numero * 3
rai = numero ** (1/2)
print(f'{c.N()}{c.branco()}O {c.magenta()}dobro {c.branco()}de {c.amarelo()}{numero} '
      f'{c.branco()}é {c.U()}{c.azul()}{dob}{c.fim()}.')

print(f'{c.N()}{c.branco()}O {c.magenta()}triplo {c.branco()}de {c.amarelo()}{numero} '
      f'{c.branco()}é {c.U()}{c.azul()}{tri}{c.fim()}.')

print(f'{c.N()}{c.branco()}A {c.magenta()}raiz quadrada {c.branco()}de {c.amarelo()}{numero} '
      f'{c.branco()}é {c.U()}{c.azul()}{rai:.2f}{c.fim()}.')
