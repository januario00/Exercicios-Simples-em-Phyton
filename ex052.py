#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo

n = int(input('Digite um numero: '))
tot = 0

for i in range (1, n + 1):
    if n % i == 0:
        tot += 1
    if tot == 2:
        print( 'o numero {} é primo'.format(i))
    else:
        print( 'o numero {} não é primo'.format(i))