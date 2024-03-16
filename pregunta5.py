def contar_digitos(numero, digito):
    # Convertir el número en una cadena para facilitar la manipulación de los dígitos
    numero_str = str(numero)
    
    # Contar la cantidad de veces que aparece el dígito en el número
    cantidad = numero_str.count(str(digito))
    
    return cantidad

# Solicitar al usuario que ingrese un número y un dígito
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese un dígito: "))

# Llamar a la función y mostrar el resultado
cantidad_digitos = contar_digitos(numero, digito)
print("Cantidad de veces", digito, "en el número:", cantidad_digitos)

