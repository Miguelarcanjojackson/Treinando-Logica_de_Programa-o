import os 

os.system("cls")

print("programa sustentavel")

hora_atv_fisica = int(input("Digite quantas horas de atividade fisica voçe fez no mês = "))

if hora_atv_fisica <= 10:

    total_de_pontos = hora_atv_fisica * 2
    valor_total = total_de_pontos * 0.05

    print(f"O total de pontos que obteve foi de = {total_de_pontos} e o valor arrecadado foi de = {valor_total}")

if hora_atv_fisica > 10 and hora_atv_fisica <= 20:

    total_de_pontos = hora_atv_fisica * 5
    valor_total = total_de_pontos * 0.05

    print(f"O total de pontos que obteve foi de = {total_de_pontos} e o valor arrecadado foi de = {valor_total}")

if hora_atv_fisica >20:

    total_de_pontos = hora_atv_fisica * 10
    valor_total = total_de_pontos * 0.05
   
    print(f"O total de pontos que obteve foi de = {total_de_pontos} e o valor arrecadado foi de = {valor_total}")



