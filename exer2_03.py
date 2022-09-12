#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

maca = int(input("Digite a quantida de maçã: "))
if (maca < 12):
    valor01 = float(maca * 1.30)
    print(f"Custo total das maçãs: R${valor01}")

else:
    valor02 = float(maca * 1)
    print(f"Custo total das maçãs: R${valor02}")
