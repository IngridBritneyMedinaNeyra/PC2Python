def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    
    # Iterar sobre los posibles divisores del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Si el número es divisible por algún número menor o igual a su raíz cuadrada, no es primo
    
    return True  # Si no se encontró ningún divisor, el número es primo

# Solicitar al usuario que ingrese un número para verificar si es primo
numero = int(input("Ingrese un número para verificar si es primo: "))

# Llamar a la función y mostrar el resultado
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
