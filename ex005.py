# Faça um programa que leia o numero inteiro e mostre na tela o seu numero sucessor e seu antecessor

a = (int(input('Digite um numero: ')))
ant = a-1
suc = a +1

print ('Analisando o valor digitado',a,',seu numero antecessor é',ant,'e seu sucessor é o numero ',suc)

# outra alternativa para retorno de tela em codigo é
#print ('Analisando o valor digitado {}, seu antecessor é {} e o sucessor é {}'.format(a,(ant),(suc)))