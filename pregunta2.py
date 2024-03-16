# Definir la función para construir el patrón
def construir_patron(filas):
    # Iterar sobre el número de filas
    for i in range(filas):
        # Imprimir '*' i veces en cada fila
        print('* ' * (i + 1))
    
    # Iterar sobre el número de filas en orden inverso, comenzando desde el segundo último hasta el primero
    for i in range(filas - 1, 0, -1):
        # Imprimir '*' i veces en cada fila
        print('* ' * i)

# Llamar a la función y pasar el número de filas como argumento
construir_patron(5)
