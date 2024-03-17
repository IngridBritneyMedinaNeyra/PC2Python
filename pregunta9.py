def omitir_vocales(cadena):
    # Definir las vocales en mayúsculas y minúsculas
    vocales = "aeiouAEIOU"
    
    # Inicializar una cadena vacía para almacenar el resultado
    resultado = ""
    
    # Iterar sobre cada carácter en la cadena de entrada
    for char in cadena:
        # Verificar si el carácter no es una vocal
        if char not in vocales:
            # Agregar el carácter al resultado
            resultado += char
    
    return resultado

# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Llamar a la función y mostrar el resultado
texto_sin_vocales = omitir_vocales(texto)
print("Texto sin vocales:", texto_sin_vocales)
