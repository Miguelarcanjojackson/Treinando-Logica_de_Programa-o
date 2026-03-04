import os 
import sys
os.system("cls")

tipo_do_carro = input("Digite o tipo do carro = ").lower()

if tipo_do_carro != "popular" and  tipo_do_carro != "luxo": # IF para validar o tipo do carro caso seja diferente das opçoes ele vai exibir uma msg e parar 
    
      print("Dado Invalido \n Escreva uma das opções a seguir = popular ou luxo...") 
      sys.exit()


kilometros_rodados = int(input("Quantos Km foram percorridos = "))

aluguel_dias = int(input("Quanto dias de aluguel = "))

if tipo_do_carro == "popular":
    
    valor_aluguel_total_popular = aluguel_dias * 90

    if kilometros_rodados <= 100:

        valor_total_km_rodados = kilometros_rodados * 0.20

        valor1_total_de_tudo_popular = valor_aluguel_total_popular + valor_total_km_rodados
        
        print(f"Valor total á pagar é = {valor1_total_de_tudo_popular:.2f} R$")

    if kilometros_rodados > 100:

        valor_total_km_rodados = kilometros_rodados * 0.10

        valor2_total_de_tudo_popular = valor_aluguel_total_popular + valor_total_km_rodados

        print(f"Valor total á pagar é = {valor2_total_de_tudo_popular:.2f} R$")

if tipo_do_carro == "luxo":
      
        valor_aluguel_total_luxo = aluguel_dias * 150

        if kilometros_rodados <= 200:
             
             valor_total_km_rodados_luxo = kilometros_rodados * 0.30

             valor_total_de_tudo_luxo = valor_aluguel_total_luxo + valor_total_km_rodados_luxo

             print(f"Valor total á pagar é = {valor_total_de_tudo_luxo:.2f} R$")

        if kilometros_rodados > 200:
             
             valor_total_km_rodados_luxo_2 = kilometros_rodados * 0.25

             valor_total_de_tudo_luxo_2 = valor_aluguel_total_luxo + valor_total_km_rodados_luxo_2

             print(f"Valor total á pagar é = {valor_total_de_tudo_luxo_2:.2f} R$")
           
        

        


    
