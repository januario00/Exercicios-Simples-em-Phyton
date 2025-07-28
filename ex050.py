## Desenvolva um progra,a que leia seis numeros inteiros e mostre a soma
## apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o

soma = 0
cont = 0
print('Digite seis valores')
for i in range (1 , 7):
        n= int(input('Digite o {}° valor: '.format(i)))
        if n % 2 == 0:
            soma += n
            cont += 1
print('A soma dos números que você informou foi de',soma)
