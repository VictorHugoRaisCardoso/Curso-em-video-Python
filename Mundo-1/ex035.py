from funcoes import c
s1 = float(input(f'{c.magenta()}Primeiro segmeto{c.fim()}: '))
s2 = float(input(f'{c.azul()}Segundo segmento{c.fim()}: '))
s3 = float(input(f'{c.amarelo()}Terceiro segmento{c.fim()}: '))

if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print(f'Estes seguimentos {c.azul()}{c.U()}podem formar um triângulo{c.fim()}')
else:
    print(f'Estes seguimentos {c.azul()}não podem formar um triângulo{c.fim()}')
