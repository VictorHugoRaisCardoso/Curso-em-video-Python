from math import sqrt, pow
"""cop = float(input('Informe o Cateto Oposto: '))
cad = float(input('Informe o Cateto Adjacente: '))
hp = math.hypot(cop, cad)
print(f'A Hipotenuza do Cateto oposto {cop} e Cateto Adjacente {cad} é {hp:.2f}')"""

"""co = float(input('Informe o Cateto Oposto: '))
ca = float(input('Informe o Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenuza vai medir {hi:.2f}')"""

co = float(input('Informe o Cateto Oposto: '))
ca = float(input('Irforme o Cateto Adjacente: '))
hi = sqrt(pow(co, 2) + pow(ca, 2))
print(f'A hipotenuza vai medir {hi:.2f}')
