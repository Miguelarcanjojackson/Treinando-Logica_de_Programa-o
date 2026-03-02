import os 

os.system("cls")

velocidade_carro = int(input("Qual foi a velocidade do carro pecorrida???"))

multa = velocidade_carro * 5.00

if velocidade_carro > 80:
    print(f"Voçe foi multado por excesso de velocidade\n velocidade = {velocidade_carro} km \n Sua multa é {multa:.2f} R$")
else:
    print("Voçe não foi multado")