import os 

os.system("cls")

ano_nascimento = int(input("Digite o ano em que voçe nasceu = "))

idade = 2026 - ano_nascimento

if idade < 18:
    quantos_falta = 18 - idade
    print(f"Daqui há {quantos_falta} anos, é o seu alistamento")

elif idade > 18:
    tempo_pasou = idade - 18
    print(f"Ja se passaram {tempo_pasou} anos do seu alistamento")
