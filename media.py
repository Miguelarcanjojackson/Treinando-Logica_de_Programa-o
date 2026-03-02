import os
os.system("cls")

peso = float(input("Digite seu peso"))

altura = float(input("Digite sua altura"))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso")
    print(f"{imc:.2f}")
    
    
elif imc <= 24.9:
    print("Peso ideal(parabéns)")
    print(f"{imc:.2f}")
    
    
if imc > 25.0 and imc < 29.9:
    print("Levemente acima do peso")
    print(f"{imc:.2f}")
    
    
if imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau 1")
    print(f"{imc:.2f}")
    
    
if imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau 2(severa)")
    print(f"{imc:.2f}")
    
    
if imc >= 40:
    
    
    print("Obesidade 3 (morbida)")
    print(f"{imc:.2f}")
    