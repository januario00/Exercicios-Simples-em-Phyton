print (' >>>>> MEDIDAS CALCULADAS <<<<<<< ')
medida = float(input('Digite a distancia em metros: '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000

print ('A medida de {}m corresponde a :\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(medida,km,hm,dam,dm,cm,mm))

#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
