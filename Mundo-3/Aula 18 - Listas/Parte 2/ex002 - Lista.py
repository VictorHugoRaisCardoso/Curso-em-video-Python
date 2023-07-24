num = [[],[]]
for n in range(0, 7):
    i = int(input(f"Digite o {n +1}º numero: "))
    if i % 2 == 0:
        num[0].append(i)
    else:
        num[1].append(i)
num[1].sort()
num[0].sort()
print("=" * 60)
print(f"Os valores pares digitados foram: {num[0]}")
print(f"Os valores impares digitados foram: {num[1]}")
