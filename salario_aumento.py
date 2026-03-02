import os

os.system("cls")

salario_funcionario = float(input("Digite o seu salario"))

porcentagem = 0.15

aumento = salario_funcionario * porcentagem

salario_final = salario_funcionario + aumento

print(f"O salario do funcionario aumentou 15% teve um aumento de {aumento}")
print(f"Seu salario atualizado é {salario_final:.2f}")



