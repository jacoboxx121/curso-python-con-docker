
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if (num1 % 2 == 0) and (num2 % 2 == 0):
    print(f"{num1} y {num2} son pares")
elif (num1 % 2 == 0) and (num2 % 2 != 0):
    print(f"{num1} es par")
elif (num1 % 2 != 0) and (num2 % 2 == 0):
    print(f"{num2} es par")
else:
    print(f"{num1} y {num2} son impares")
