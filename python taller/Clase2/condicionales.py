#Condicionales

dato = int(input("Ingrese un numero: "))
if dato > 0:
    print("El numrto es positivo")
elif dato < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

if dato % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")