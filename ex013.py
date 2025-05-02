# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = (float(input('Digite o valor do seu salario: R$')))
desconto = (int(input('Digite a porcentagem do desconto aplicado:')))


aumento = salario * (desconto/100)
novoSalario = salario + aumento

print ('O valor do salario com aumento de {}% no valor é de R${:.2f}'.format(desconto,novoSalario))