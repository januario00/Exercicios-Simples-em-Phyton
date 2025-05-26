#Faça um programa que leia o nome completo de uma pessoa , mostrando em seguida o primeiro e o ultimo nome separadamente.


nome = str(input('Digite seu nome completo: ')).strip()

n = nome.split()

print ('Muito prazer em te conhecer',nome,'!')
print ('O primeiro nome é',n[0])
print ('E o ultimo nome é',n[len(n)-1])



