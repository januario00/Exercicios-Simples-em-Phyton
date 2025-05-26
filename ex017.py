#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
#Calcule e mostre o comprimento da hipotenusa

from math import hypot

a = (float(input("Digite o valor do cateto oposto: ")))
b = (float(input("Digite o valor do cateto adjacente: ")))

h = hypot(a,b)
print("Valor da hipotenusa é ",h)

