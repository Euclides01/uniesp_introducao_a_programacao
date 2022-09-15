#Faça um programa que mostre as tabuadas dos números de 1 a 10.
for numero in range(1, 11):
    print(f"Tabuada do {numero}")
    for numero2 in range(1, 11):
        resultado = numero * numero2
        print(f"{numero} x {numero2} = {resultado}")


#Faça um programa que mostre as tabuadas dos números de 1 a 10.

for numero in range(1, 10):
    print(f"Tabuado do {numero}")
    for numero2 in range(10, 0, -1):
            numero3 = numero * numero2
            print(f"{numero} x {numero2} = {numero3}")