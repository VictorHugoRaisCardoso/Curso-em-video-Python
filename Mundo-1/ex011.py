B = float(input('Largura da parede: '))
H = float(input('Altura da parede: '))
A = B * H
T = A / 2
print(f'Sua parede tem a dimensão de {B:.1f} x {H:.1f} e a sua Área é de {A:.3f}m².')
print(f'Para pintar essa parede, você precisará de {T:.1f}L de tinta.')
