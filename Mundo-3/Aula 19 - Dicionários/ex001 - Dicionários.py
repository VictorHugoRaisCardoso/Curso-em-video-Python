aluno = dict()
aluno["NOME"] = str(input('Nome: ')).title()
aluno["MÉDIA"] = float(input('Média: '))
if aluno["MÉDIA"] >= 7:
    aluno["STATUS"] = "Aprovado"
elif aluno["MÉDIA"] > 5 and aluno["MÉDIA"] < 7:
    aluno["STATUS"] = "Recuperação"
elif aluno["MÉDIA"] <= 5:
    aluno["STATUS"] = "Reprovado"
print("-=" * 30)
for k, v in aluno.items():
    print(f'  - {k}: {v}')
