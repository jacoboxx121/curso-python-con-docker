'''
Ejemplo de funciones en Python
'''

# ------------------------------------------------------------------
# COMPARACIÓN RÁPIDA: Funciones en C++ (comentadas)
# ------------------------------------------------------------------
# En C++ primero se declara el prototipo y luego se define la función:
#   void sumar(int a, int b);        // Prototipo
#   int main() {
#       cout << sumar(5,10);
#   }
#   void sumar(int a, int b){        // Definición
#       return a + b;
#   }

# ------------------------------------------------------------------
# Mismo ejemplo, pero en Python
# ------------------------------------------------------------------

# Guardamos dos números en variables
a = 2
b = 3

# ------------------------------------------------------------------
# Función SUMAR
# ------------------------------------------------------------------
# "def" indica que vamos a crear una función.
# Los parámetros se llaman "a" y "b" dentro de la función.
def sumar(a, b):
    return a + b  # Devuelve la suma de los dos valores recibidos

# Llamamos (ejecutamos) la función y mostramos el resultado
print("Resultado de la suma:", sumar(a, b))

# ------------------------------------------------------------------
# Función RESTAR
# ------------------------------------------------------------------
def restar(a, b):
    return a - b  # Devuelve la resta de los dos valores recibidos

# Llamamos a la función y mostramos el resultado
print("Resultado de la resta:", restar(a, b))

# ------------------------------------------------------------------
# Resumen en lenguaje sencillo
# 1. "def nombre(parámetros):" crea una función.
# 2. "return" devuelve el resultado.
# 3. Para usar la función basta con escribir su nombre y entre paréntesis
#    los valores que necesita: sumar(2, 3).