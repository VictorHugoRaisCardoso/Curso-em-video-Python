from datetime import datetime
ano = datetime.now().year
pessoa = {}
pessoa['NOME'] = str(input("NOME: "))
nasc = int(input("DATA DE NASCIMENTO: "))
pessoa['IDADE'] = (ano - nasc)
pessoa['CTPS'] = int(input("Nº da CTPS (0 não tem): "))
if pessoa["CTPS"] != 0:
    pessoa["ANO DO REGISTRO"] = int(input("ANO DO REGISTRO DE EMPREGO: "))
    pessoa["SALARIO"] = float(input("SALÁRIO: "))
    pessoa["APOSENTADORIA"] = (pessoa["IDADE"] + (35 - (ano - pessoa["ANO DO REGISTRO"])))
print('=' * 60)
for c, v in pessoa.items():
    print(f'   - {c}: {v}')
