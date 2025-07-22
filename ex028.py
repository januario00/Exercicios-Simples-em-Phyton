#Escreva um programa que faça o computador "pensar" em um numero interio entre o 0 e 5 e peça para o usuario
# tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuario
# venceu ou perdeu.

from random import randint
from time import sleep

print('🔮✨ TAROT DE NUMERO 🔮✨️')
print('🃏 Olá, quer tentar acertar o numero?🃏')

sorteado = randint(0,5)

numero = int(input('Digite um numero entre 0 e 5: '))
print('SORTEANDO ...')
sleep(3)

if numero == sorteado:
    print('Você acertou 🎉🎊🥳🎈🍾')
elif numero <0 or numero > 5:
    print('Número Invalido')
else:
    print ('Não foi dessa vez, o numero correto era',sorteado)
