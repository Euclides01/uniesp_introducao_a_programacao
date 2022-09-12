#Crie um programa em Python que solicite um número do usuário, depois some este número com 1357, multiplique por 8, divida por 5 e eleve ao quadrado.

numero = int(input("Digite um número: "))
soma = numero + 1357
multiplica = soma * 8
divide = multiplica/5
eleva = divide ** 2
resultado = (((numero + 1357)*8)/5)**2
print(f"Resultado da soma: {soma}")
print(f"Resultado da multiplicação: {multiplica}")
print(f"Resultado da divisão: {divide}")
print(f"Resultado da potência: {eleva}")
print(f"Resultado final: {resultado}")