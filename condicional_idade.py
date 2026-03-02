import os 

os.system("cls")

matricula_usuario = int(input("Digite sua matricula(Empregado)"))

ano_nascimento_usuario = int(input("Digite o ano em que voçe nasceu "))

anos_trabalhando_usuario = int(input("Quanto tempo de trabalho?"))

idade_usuario = 2026 - ano_nascimento_usuario

if idade_usuario < 35 and anos_trabalhando_usuario >= 30:
    print(f"Não tem logica\n voçe ter menos idade = {idade_usuario} \n e ter trabalhado = {anos_trabalhando_usuario} anos")

elif idade_usuario >= 65 or anos_trabalhando_usuario >= 30:
    print(f"sua matricula é = {matricula_usuario}\n idade = {idade_usuario}\n tempo trabalhado = {anos_trabalhando_usuario}\n Requerer aposentadoria ou Não requerer?")

else:
    print(f"Voçe não atingiu as espeçificações \n idade = {idade_usuario} \n tempo trabalhado = {anos_trabalhando_usuario}")
    print("para estar apto, pelo menos tem que ter 65 anos ou ter trabalhado pelo menos 30 anos")