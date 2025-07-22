from time import sleep

print('-='*20)
print('APROVAÇÃO DE EMPRESTIMO BANCÁRIO')
print('-='*20)
print('VAMOS COMEÇAR?')
sleep(3)
casa =float(input("Digite o valor valor da casa que deseja comprar: "))
salario = float(input('Digite o valor do seu salário atual:'))
anos = int(input('Em quantos anos você pretende quitar o valor? '))

meses = anos * 12
vprestacao = casa / meses
porcentagem = salario * 0.30

if vprestacao > porcentagem:
    print ("Não será possivel realizar o a emprestimo pois o valor prosposto não condiz com as diretrizes do contrato,")
    print('O valor das parcelas ficaram de R${:.3f} por {} anos muito acima de 30% do valor da sua renda'.format(vprestacao, anos))
else :
    print ('Parabéns, seu emprestimo foi aceito')
    print('O valor das parcelas ficaram de R${:.3f} por {} anos'.format(vprestacao, anos))
