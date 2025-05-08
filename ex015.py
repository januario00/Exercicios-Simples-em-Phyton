#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15Km rodado.


km = float(input("Digite a quantidade de km percorrido: "))
d = int(input("Digite a quantidade de dias utilizados: "))

calKm = (km * 0.15)
calDia = (d * 60)
total = calDia + calKm

print("O valor baseado em seus gastos foi de",total)