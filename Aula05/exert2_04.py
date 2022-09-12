#Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
media = float((nota01+nota02)/2)

if (media < 6):
    print("Infelizmente, você não foi aprovado.")
    print(f"Sua média: {media}")

else:
    print("Parabéns, você foi aprovado.")
    print(f"Sua média: {media}")    