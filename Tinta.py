import os
os.system("cls")

largura = float(input("Digite o valor da largura"))

altura = float(input("Digite o valor da altura da parede"))

area = largura * altura
quntd_tinta = area / 2

print(f"Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}")

print(f"A quantidade de tinta necessaria é {quntd_tinta:.0f}")
