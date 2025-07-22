

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))


if num1 > num2 and num1 > num3:
    print(f"O maior número é {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é {num2}")
elif num3 > num1 and num3 > num2:
    print(f"O maior número é {num3}")
else:
    print("Todos os números são iguais ou não há um único maior.")

if num1 < num2 and num1 < num3:
    print(f"O menor número é {num1}")
elif num2 < num1 and num2 < num3:
    print(f"O menor número é {num2}")
elif num3 < num1 and num3 < num2:
    print(f"O menor número é {num3}")
else:
    print("Todos os números são iguais ou não há um único menor.")  