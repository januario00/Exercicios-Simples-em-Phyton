#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.


numero = int(input('Digite um numero de 0 a 9999: '))

unidade = numero //1 % 10
dezena = numero //10 % 10
centena = numero //100 % 10
milhar = numero //1000 % 10

print ('Unidade:',unidade)
print ('Dezena:',dezena)
print ('Centena:',centena)
print ('Milhar:',milhar)

