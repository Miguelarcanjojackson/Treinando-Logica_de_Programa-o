import os

os.system("cls")

numero = int(input("Digite um numero"))

par_ou_impar = numero % 2

if numero % 2 == 0:
    print(f"O numero é par = {numero} \n porque o resto da divisão é =  {par_ou_impar}")
else:
    print(f"O numero é impar = {numero} \n porque o resto da divisão é = {par_ou_impar}")