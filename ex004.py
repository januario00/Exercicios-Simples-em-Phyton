# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e mostre todas as informaçõe possiveis sobre ela;


a = input('Digite algo: ')
print ('O tipo primitivo desse valor é: ', type(a))
#sempre o tipo primitivo do que foi digitado retorna STR se nao for definido o tipo antes do input
#nesse exercicio o objetivo é voce descobrir o que foi digitado pelas caracteristicas citadas sem precisar
#ser definido o tipo do que foi digitado
print ('Só tem espaços? ', a.isspace())
print ('É alfabetico? ', a.isalpha())
print ('É alfanumerico? ', a.isalnum())
print ('Esta em maiusculos?',a.isupper())
print ('Esta em minusculos?',a.islower())
print ('Esta capitalizada?',a.istitle())


