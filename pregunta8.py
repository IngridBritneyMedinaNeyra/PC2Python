def factorial(numero):
    # Verificar si el número es negativo
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    
    # Inicializar el factorial como 1
    resultado = 1
    
    # Calcular el factorial iterativamente
    for i in range(1, numero + 1):
        resultado *= i
    
    return resultado

# Solicitar al usuario que ingrese un número para calcular su factorial
numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))

# Llamar a la función y mostrar el resultado
print("El factorial de", numero, "es:", factorial(numero))
