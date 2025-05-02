

largura = (float(input('Digite a largura da parede:')))
altura = (float(input("Digite a altura da parede:")))

area = largura*altura
litro = area/2

print('Sua parede tem a dimenção de {} x {}, e a sua AREA é de {}².'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(litro))

#Faça um programa que leia a largura e altura de uma parede em metros. Calcule a sua area e a quantidade de tinta necessaria
#para pinta-la. Sabendo que cada litro de tinta pinta uma area de 2m²