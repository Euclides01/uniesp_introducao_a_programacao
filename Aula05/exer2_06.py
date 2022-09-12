#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

numero01 = float(input("Digite um número:"))
numero02 = float(input("Digite outro número (precisa ser diferente do anterior):"))

if (numero01 > numero02):
    print(f"Ordem crescente dos dois números: {numero01}, {numero02}")

elif (numero01 < numero02):
    print(f"Ordem crescente dos dois números: {numero02}, {numero01}")

else:
    print("Por favor, digite dois números diferentes!")