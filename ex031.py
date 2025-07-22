print ("BEM VINDO AO PROGRAMA DE CÁLCULO DE DISTÂNCIA")

print("Lembrando que o valor cobrado para viagens até 200km é de R$0,50 por KM e acima disso é de R$0,45 por KM.")


distancia = float(input("Digite a distância em KM "))

curta_distancia = distancia * 0.50
longa_distancia = distancia * 0.45

if distancia <= 200:
    print(f"O valor da sua viagem é de R${curta_distancia:.2f}")
else:
    print(f"O valor da sua viagem é de R${longa_distancia:.2f}")
