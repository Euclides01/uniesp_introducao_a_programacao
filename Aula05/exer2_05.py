#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

numero01 = float(input("Digite um número:"))
numero02 = float(input("Digite outro número (precisa ser diferente do anterior):"))

if (numero01 > numero02):
    print(f"O número {numero01} é maior!")

elif (numero01 < numero02):
    print(f"O número {numero02} é maior!")

else:
    print("Por favor, digite dois números diferentes!")