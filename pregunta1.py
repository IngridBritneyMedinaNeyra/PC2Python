# Definir la función para encontrar los números divisibles por 7 y múltiplos de 5
def encontrar_numeros():
    # Lista para almacenar los números encontrados
    numeros_encontrados = []

    # Iterar a través del rango de 1500 a 2700
    for numero in range(1500, 2701):
        # Verificar si el número es divisible por 7 y múltiplo de 5
        if numero % 7 == 0 and numero % 5 == 0:
            # Agregar el número a la lista de números encontrados
            numeros_encontrados.append(numero)

    # Retornar la lista de números encontrados
    return numeros_encontrados

# Llamar a la función y almacenar el resultado en una variable
numeros_divisibles = encontrar_numeros()

# Imprimir los números encontrados
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_divisibles)
