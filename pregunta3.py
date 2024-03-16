# Inicializar listas para almacenar números pares e impares
numeros = []
pares = []
impares = []

# Bucle while para permitir el ingreso de números hasta que el usuario decida detenerse
while True:
    respuesta = input("Desea ingresar un número? (SI/NO): ").upper()
    
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, ingrese 'SI' o 'NO'.")

# Evaluar cada número para determinar si es par o impar
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Imprimir la lista de números ingresados
print("Números ingresados:", numeros)

# Imprimir la cantidad de números pares e impares
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))
