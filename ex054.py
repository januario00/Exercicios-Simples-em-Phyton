
from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for i in range (1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    idade = atual - nasc

    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('A quantidade de pessoas maiores de idade foram de',totalmaior)
print('A quantidade de pessoas menores de idade foram de',totalmenor)

