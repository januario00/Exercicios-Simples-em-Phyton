from datetime import date

print ("OLÁ GUY")
print ("-=" * 20  )
print ("Esse ano é ano bissexto?")
print("Eu não sei , você sabe?")
print ("Se o numero digitado for 0 , o calculo será feito com o ano atual")
print ("-=" * 20  )
ano = int(input("Digite o ano:"))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano", ano, "é bissexto.")
else:
    print("O ano", ano, "não é bissexto.")