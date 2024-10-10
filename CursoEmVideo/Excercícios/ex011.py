lar = float(input('Qual a largura desta parede? '))
alt = float(input('Qual a altura desta parede? '))

área = alt * lar

print(f'Sua parede tem a dimensão de {lar}X{alt} e sua área é de {área}m².')

tinta = área / 2

print(f'Para pintar esta parede você precisa de {tinta}L.')
