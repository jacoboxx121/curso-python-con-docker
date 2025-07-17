def sumar (a, b):
    return a + b   

print("El resultado de la suma es:", sumar(5, 10))


def restar (a, b):
    return a - b

resultado = restar(10, 5)
print("El resultado de la resta es:", resultado)

def multiplicar (a, b):
    return a * b

resultado = multiplicar(5, 10)
print("El resultado de la multiplicación es:", resultado)

def dividir (a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b  

resultado = dividir(10, 5)
print("El resultado de la división es:", resultado)    