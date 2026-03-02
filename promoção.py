import os 

os.system("cls")

produto = float(input("Informe o valor do produto"))

desconto = 0.05

produto_desconto = produto * desconto
preco_final = produto - produto_desconto

print(f"O valor do produto com desconto é {preco_final:.2f}")
