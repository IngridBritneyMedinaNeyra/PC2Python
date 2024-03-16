def fibonacci(n):
    fib_sequence = [0, 1]  # Inicializar la secuencia de Fibonacci con los dos primeros números

    while True:
        # Calcular el siguiente número de Fibonacci sumando los dos últimos números de la secuencia
        next_number = fib_sequence[-1] + fib_sequence[-2]
        
        # Romper el bucle si el siguiente número excede el límite dado (en este caso, 50)
        if next_number > n:
            break
        
        # Agregar el siguiente número a la secuencia
        fib_sequence.append(next_number)
    
    return fib_sequence

# Obtener la serie de Fibonacci hasta el número 50
fibonacci_sequence = fibonacci(50)

# Imprimir la serie de Fibonacci obtenida
print("Serie de Fibonacci hasta el número 50:")
print(fibonacci_sequence)
