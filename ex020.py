#Faça um programa que sortea a ordem de apresentação de trabalhos dos alunos

from random import shuffle

lista = ["Eva","Maria","Matheus","Pedro","Jenifer","Mauricio"]
shuffle(lista)

print ("A ordem de apresentação será {}".format(lista))
