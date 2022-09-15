#Seja criativo ao desenvolver este programa.

#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
#personalizado.
#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
#convites. Imprima o nome das pessoas que não poderão comparecer.
#d. Modifique sua lista, substitua os desistentes por novos convidados.
#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

lista_jantar = ['Silvio santos', 'Ratinho', 'Maisa Silva', 'Caio Coppolla', 'Neymar']
nome = []
x = 0 
while x < len(lista_jantar):
    print("Olá" + f" {lista_jantar[x]}".upper() + ", você foi contemplo em participar do Jantar do Famosos!")
    nome = input("Digite sim para confirmar a sua presença ou não para confirmar a sua ausência: ").upper()
    x += 1



