import os 
#limpar o terminal
os.system("cls")

print("--------------------------------------------")
numero_um = float(input("Digite o primeiro numero"))
numero_dois = float(input("Digite o segundo numero"))
print("--------------------------------------------")

print("")
#calculando
soma = numero_um + numero_dois
media = (numero_um + numero_dois) / 2
produto = numero_um * numero_dois

print("---------------------------------------------")

print(f"A media dos dois numero é {media:.1f}")
print(f"A soma entre os dois numeros é {soma:.1f} ")
print(f"O produto entre dois numeros é {produto:.1f}")

print("---------------------------------------------")

if numero_um > numero_dois:
    print(f"O maior numero é {numero_um} e o menor numero é {numero_dois}")
if numero_dois > numero_um:
    print(f"O numero maior é {numero_dois} e o menor numero é {numero_um}")
    