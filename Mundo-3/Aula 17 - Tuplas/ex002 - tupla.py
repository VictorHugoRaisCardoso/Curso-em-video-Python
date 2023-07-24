brasileirao = ("Palmeiras", "Internacional", "Fluminense", "Corinthians", "Flamengo", "Athletico-PR", "Atlético-MG", "Fortaleza", "São Paulo", "América-MG", "Botafogo", "Santos", "Goiás", "Bragantino", "Coritiba", "Cuiabá", "Ceará", "Atletico-GO", "Avaí", "Juventude")
alfabetica = (sorted(brasileirao))
print(f"Os 5 primeiros colocados do Brasileirão são: ")
for i in range(0, 5):
    print(f"{i + 1} - {brasileirao[i]}")
print(f"Os 4 ultimos colocados são: ")
for i in range(16, 20):
    print(f"{i + 1} - {brasileirao[i]}")
print(f"Os times em ordem alfabetica são: {sorted(brasileirao)}")
for posicao, time in enumerate(brasileirao):
    if brasileirao[posicao] == "Fluminense":
        print(f"O {time} esta na posição {posicao + 1}")
