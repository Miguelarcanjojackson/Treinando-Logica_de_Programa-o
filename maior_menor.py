import os 
os.system("cls")

numero_um = int(input("Digite sua primeira nota "))

numero_dois = int(input("Digte sua segunda nota"))

print("------------------------------------------")

soma = numero_um + numero_dois 
media = soma / 2
produto = numero_um * numero_dois

print(f"A soma entre os numeros é {soma}")
print(f"A media entre os numeros é {media}")
print(f"O produto entre os numeros é {produto}")


if numero_um > numero_dois:
    
  maior = numero_um
  menor = numero_dois
  
  print(f"o maior numero é {maior}")
  print(f"O menor numero é {menor}")
  print("----------------------------------------")
  
elif numero_um == numero_dois:
    
    print(f"Os numeros digitados são iguais")
    print("--------------------------------------")

else:
    maior = numero_dois
    menor = numero_um
    
    print(f"O maior numero é {maior}")
    print(f"O menor numero é {menor}")
    print("---------------------------------------")
    
    
    
    
    

