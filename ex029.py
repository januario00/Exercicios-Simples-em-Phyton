#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 POR CADA Km acima do limite.

velocidade = int(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7.00

if velocidade >= 80 :
    print('Voce foi multado, terá que pagar uma multa no valor de R$',multa,'reais')
else:
    print('Esta Tudo Certo')
