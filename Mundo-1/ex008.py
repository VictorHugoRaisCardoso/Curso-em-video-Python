from time import sleep
from funcoes import c

MT = float(input(f'{c.N()}{c.U()}{c.vermelho()}Digite um valor em metros:{c.fim()} '))

KM = MT / 1000
HM = MT / 100
DAM = MT / 10
DM = MT * 10
CM = MT * 100
MM = MT * 1000

sleep(5)

print(f'''{c.branco()}{c.N()}Convertendo o valor inserdo obteremos os seguintes resultados: 
{c.azul()}{KM}Km
{HM}Hm
{DAM}Dam
{DM:.0f}Dm
{CM:.0f}Cm
{MM:.0f}mm''')
