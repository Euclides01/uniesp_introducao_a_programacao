#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

#QAE = quantidade atual em estoque
#QMAE = quantidade máxima em estoque
#QMIE = quantidade mínima em estoque de um produto
#QM = quantidade média

QAE = int(input("Digite a quantidade atual em estoque: "))
QMAE = int(input("Digite a quantidade máxima em estoque: "))
QMIE = int(input("Digite a quantidade mínima em estoque: "))
QM =  int((QMAE + QMIE)/2)

print(f"Quantidade média: {QM}")

if (QAE >= QM):
    print("Não efetuar a compra!")

else:
    print("Efetuar compra!")