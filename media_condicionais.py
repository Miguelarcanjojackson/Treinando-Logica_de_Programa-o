import os
os.system("cls")

nota_um = float(input("Digite sua primeira nota "))
nota_dois = float(input("Digite sua segunda nota"))
nota_tres = float(input("Digite sua terceira nota "))

media_final = (nota_um + nota_dois + nota_tres) / 3

if media_final < 7:
    print("Voces esta reprovado, sua media final foi",media_final)
elif media_final >=7:
    print("Voçe foi aprovado, sua media final foi ",media_final)
    