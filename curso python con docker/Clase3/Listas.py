'''
Ejemplos de listas en Python
'''

# 1. Crear una lista con diferentes tipos de datos
array = ["futbol", "Pc", 18.6, 18, [6, 7, 10.4], True, False]
print(array)                    # Mostrar la lista completa

# 2. Acceder a elementos individuales
print(array[0])                 # Primer elemento → "futbol"
print(array[4])                 # Quinto elemento → [6, 7, 10.4]

# 3. Obtener un "trozo" (slice) de la lista
#    Desde la posición 0 hasta la 3 sin incluir la 3
print(array[0:3])               # ["futbol", "Pc", 18.6]

# 4. Ver cuántos elementos tiene la lista
print(len(array))               # 7

# 5. Añadir un elemento al final
array.append(66)                # Añade 66 al final
print(array)

# 6. Insertar un elemento en una posición concreta
#    Insertamos "baloncesto" en la posición 2
array.insert(2, "baloncesto")
print(array)

# 7. Añadir varios elementos de golpe
array.extend(["tenis", "natación"])  # Añade dos strings al final
print(array)

# 8. Eliminar la primera aparición de un valor concreto
array.remove("Pc")              # Borra "Pc" (solo la primera vez)
print(array)

# 9. Eliminar el último elemento
array.pop()                     # Borra "natación"
print(array)

# 10. Eliminar un elemento en una posición exacta
array.pop(2)                    # Borra el elemento que está en la posición 2
print(array)

# 11. Vaciar toda la lista
array.clear()
print(array)                    # → []

# 12. Volver a crear la lista original
array = ["futbol", "Pc", 18.6, 18, [6, 7, 10.4], True, False]

# 13. Crear otra lista
array2 = ["baloncesto", "tenis", "natación"]

# 14. Unir (concatenar) dos listas
array3 = array + array2         # Combina los elementos de ambas listas
print(array3)

# 15. Comprobar si un elemento existe en la lista
print("futbol" in array3)       # Devuelve True

# 16. Saber en qué posición está un elemento
print(array3.index("baloncesto"))  # Devuelve el índice (posición) del primer "baloncesto"

# 17. Contar cuántas veces aparece un elemento
print(array3.count("natación"))    # Devuelve 1

# 18. Invertir el orden de los elementos
array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array4.reverse()                # Ahora será [10, 9, 8, ..., 1]
print(array4)

# 19. Ordenar los elementos de menor a mayor
array5 = [1, 3, 2, 4, 6, 5, 8, 7, 9, 10]
array5.sort()                   # Ahora queda [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array5)