import os 
os.system("cls")

print(" Exibindo programa............\n")

dias_totais = int(input("Digite a quantidade de dias que voçe trabalhou"))  

quantidade_horas = dias_totais * 8

salario_final = quantidade_horas * 25

print(f"Seu salario por mes é {salario_final:.2f}")
