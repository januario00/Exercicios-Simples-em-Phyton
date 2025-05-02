produto = (float(input('Qual o valor do produto?')))
reajuste = produto * (5/100)
total = produto - reajuste


print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto,total))

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.