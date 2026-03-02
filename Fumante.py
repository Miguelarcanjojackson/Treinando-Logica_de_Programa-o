import os 

os.system("cls")

cigarros = int(input("Quanto cigarros vc fuma por dia =="))

anos_fumados = int(input("Voçe fuma por quantos anos =="))

total_de_dias= anos_fumados * 365

totais_cigarro = cigarros * total_de_dias

total_minutos_perdido = totais_cigarro * 10

total_de_dias_perdidos = total_minutos_perdido / 1440

print(f"Voçe fumava {cigarros} cigarro por dia")
print(f"Voçe fumou por {anos_fumados} anos")
print(f"Voçe fumou durante {total_de_dias} dias")
print(f"Num total,voçe fumou {totais_cigarro} cigarro")
print(f"Voçe perdeu {total_minutos_perdido} minutos perdidos")
print(f"Gerando num total de dias perdidos foi {total_de_dias_perdidos:.0f}")



