#Crie um programa que leia o nome completo de uma pessoa e mostre :
# - O nome com todas as letras maiusculas ✅
# - O nome com todas as letras minusculas ✅
# - Quantas letras ao todo (sem considerar espaços)✅
## Quantas letras tem o primeiro nome✅


nome = str(input('Digite seu nome: '))

primeiro = nome.split()
nome_junto = (nome.replace(" ",""))

print ('Seu nome em letras maiusculas é:',nome.upper()) #Nome todo com letras maiusculas
print ('Seu nome em letras minusculas é:',nome.lower()) #Nome todo com letras minusculas
print ('A quantidade de letras do seu nome completo é:',(len(nome_junto))) #Contagem de letras sem a contagem de espaços
print ('A quantidade de letras que seu primeiro nome possui é:',(len(primeiro[0])))


# nome = str(input('Digite seu nome completo:')).strip()
# print('Analisando seu nome...')
# print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
# print('Seu nome em letras minusculas é {}'.format(nome.lower()))
# print ('Seu nome tem ao todo {} letras'.format(len(nome) - (nome.count(' ')))
# print ('Seu primeiro nome tem {} letras'. format(nome.find(' ')))

