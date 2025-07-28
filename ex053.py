#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
#Desconsiderando os espaços


frase = str(input('Digite uma frase para verificarmos se é um palíndromo: ')).strip().upper()

palavras = frase.split()
junto =''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1 ,-1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

