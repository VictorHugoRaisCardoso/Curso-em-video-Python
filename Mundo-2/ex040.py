nota_1 = float(input('Primeira Nota: '))
nota_2 = float(input('Segunda Nota: '))
print()
media = (nota_1 + nota_2) / 2
print(f'Tirando {nota_2:.1f} e {nota_1:.1f}, a média do aluno é {media:.1f}')
if media < 4.9:
    print('O aluno está REPROVADO.')
elif 5 <= media < 6:
    print('O aluno está em RECUPERAÇÃO.')
elif 6 >= media:
    print('O aluno está APROVADO.')
