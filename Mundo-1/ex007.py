from time import sleep
from funcoes import c
from emoji import emojize

n1 = float(input(f'{c.N()}{c.magenta()}Primeira nota do aluno{c.fim()}: '))
n2 = float(input(f'{c.N()}{c.magenta()}Segunda nota do aluno{c.fim()}: '))
media = (n1 + n2) / 2

sleep(0.8)
print(f'{c.neg()}{c.branco()}{c.N()}PROCESSANDO NOTAS...{c.fim()}')

# Média Rasoavel
if 6.0 <= media < 8.0:
    sleep(5)
    print(emojize(f'{c.verde()}:3rd_place_medal: {c.N()}{c.branco()}Sua média foi positiva,'
                  f' você está com {media:.1f}, mas eu acredito que você pode fazer'
                  f' muito mais!{c.fim()}', use_aliases=True))

# Média Alta
elif 8.0 <= media < 10.0:
    sleep(5)
    print(emojize(f'{c.cinza()}:2nd_place_medal: {c.branco()}{c.N()}Você ficou a poucos passos da'
                  f' perfeição, meus prarabéns, a sua média foi {c.azul()}{c.U()}'
                  f'{media:.1f}{c.fim()}{c.branco()}!', use_aliases=True))

# Média Perfeita
elif media == 10.0:
    sleep(5)
    print(emojize(f'{c.amarelo()}:1st_place_medal: {c.branco()}{c.N()}Seus esforços'
                  f' te levaram a perfeição, meus parabéns, sua média foi '
                  f'{c.azul()}{c.U()}{media:.1f}{c.fim()}{c.branco()}!{c.fim()}', use_aliases=True))

# A Baixo Da Média
elif media < 6.0:
    sleep(5)
    print(emojize(f'{c.vermelho()}:cross_mark: {c.branco()}{c.N()}Se esforce mais, sua média foi'
                  f' {c.U()}{c.vermelho()}{media:.1f}{c.fim()}{c.branco()},'
                  f' isto não é bom!!! {c.magenta()}'
                  f':anxious_face_with_sweat:{c.fim()}', use_aliases=True))
    sleep(5)
    print(emojize(f'{c.branco()}{c.N()}Estaremos te encaminhando para uma'
                  f' turma de reforço dos estudos. Seja inteligente, leia livros '
                  f'{c.ciano()}:books:', use_aliases=True))
    sleep(5)
    print(emojize(f'{c.branco()}{c.N()}Te desejo muito boa sorte, nos vemos em breve! {c.amarelo()}:OK_hand:',
                  use_aliases=True))

else:
    print(f'Desculpe mas não conseguimos reconhecer os valor informado!')
