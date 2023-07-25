from funcoes import c

numero = int(input(f'{c.N()}{c.azul()}Digite um {c.N()}{c.U()}{c.amarelo()}número{c.fim()}: '))
sucessor = numero + 1
antecessor = numero - 1
print(f'{c.N()}{c.magenta()}O número {c.verde()}{numero} {c.magenta()}tem como antecessor o {c.vermelho()}{antecessor} '
      f'{c.magenta()}e como sucessor o {c.amarelo()}{sucessor}{c.fim()}.')
