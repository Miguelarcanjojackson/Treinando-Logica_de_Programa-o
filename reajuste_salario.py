import os 
import sys
os.system("cls")

sexo = input("Digite seu genero = masculino | feminino = ").lower().strip()

if sexo != "feminino" and sexo != "masculino":
     print("Dado invalido")
     sys.exit()

salario_do_funcionario = float(input("Digite seu salario atual = "))

tempo_trabalho_na_empresa = int(input("Digite o tempo de trabalho na empresa ="))


    

if sexo == "feminino":

    if tempo_trabalho_na_empresa < 15:
        novo_salario = salario_do_funcionario + (salario_do_funcionario * 0.05)
        print(f"Seu novo salario é = {novo_salario:.2f} R$")
    
    if tempo_trabalho_na_empresa >= 15 and tempo_trabalho_na_empresa <= 20:
         novo_salario = salario_do_funcionario + (salario_do_funcionario * 0.12)
         print(f"Seu novo salario é = {novo_salario:.2f} R$")
    
    if tempo_trabalho_na_empresa > 20:
         novo_salario = salario_do_funcionario + (salario_do_funcionario * 0.23)
         print(f"Seu novo salario é = {novo_salario:.2f} R$")

if sexo == "masculino":
     
     if tempo_trabalho_na_empresa < 20:
          novo_salario = salario_do_funcionario + (salario_do_funcionario * 0.03)
          print(f"Seu novo salario é = {novo_salario:.2f} R$")

     if tempo_trabalho_na_empresa >= 20 and tempo_trabalho_na_empresa <=30:
          novo_salario = salario_do_funcionario + (salario_do_funcionario * 0.13)
          print(f"Seu novo salario é = {novo_salario:.2f} R$")

     if tempo_trabalho_na_empresa > 30:
          novo_salario = salario_do_funcionario + (salario_do_funcionario * 0.25)
          print(f"Seu novo salario é = {novo_salario:.2f} R$")
          
