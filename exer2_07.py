#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

mum_conta = int(input("Olá, digite o número da sua conta: "))
print("Agora, digite:")
saldo = float(input("Saldo: "))
debito = float(input("Débito: "))
credito = float(input("Crédito: "))
saldo_atual = float(saldo - debito + credito)

print(f"Seu saldo atual: {saldo_atual}")
if (saldo_atual >= 0):
    print("Saldo positivo!")

else:
    print("Saldo negativo!")