import os 

os.system("cls")

km_pecorridos = float(input("Quantos km voçe pecorreu?"))
dias_alugados = int(input("Por quantos dias voçe alugou o carro"))

total_alugado = dias_alugados * 90
total_km = km_pecorridos * 0.20

total_a_pagar = total_alugado + total_km

print(f"O preço total a pagar é {total_a_pagar:.2f}")

