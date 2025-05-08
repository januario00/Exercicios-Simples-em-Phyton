#Escreva um programa que converta uma temperatura digitando em graus Celcius e converta para graus Fahrenheit

c = float(input("Digite a temperatura atual: "))

f = c * 9 / 5 + 32
print ("A temperatura atual é {}°F".format(f))
