'''
Ejemplo estructura de control for
'''

# Ejemplo en C++
# for (int i = 0; i < 10; i++) {
#     cout << "El valor de i es: " << i << endl;
# }

# contador = 10  # Guardamos en una variable cuántas vueltas queremos dar
# for i in range(contador):  # range(10) produce los números 0,1,2,...,9
#     print("El valor de i es:", i)  # Mostramos el número actual
# print("Fin del bucle for")  # Cuando el for termina, se ejecuta esta línea

# ------------------------------------------------------------------
# Ejemplo trabajando con una lista (array)
# ------------------------------------------------------------------

# Creamos una lista que contiene diferentes tipos de datos
array = ["futbol", "Pc", 18.6, 18, [6, 7, 10.4], True, False]

# len(array) nos dice cuántos elementos tiene la lista
print(len(array))  # Imprime: 7  (porque hay 7 elementos)

# Añadimos otro elemento al final de la lista
array.append("PC")

# Mostramos la lista ya con el nuevo elemento
print(array)  # Salida: ['futbol', 'Pc', 18.6, 18, [6, 7, 10.4], True, False, 'PC']

# Recorremos la lista usando un for tradicional con índices
for i in range(len(array)):  # i tomará los valores 0,1,2,...,hasta la última posición
    print("El valor del array es:", array[i])  # Imprimimos el elemento que está en la posición i

# Mensaje que aparece cuando el bucle ha terminado
print("Fin del bucle for con lista")