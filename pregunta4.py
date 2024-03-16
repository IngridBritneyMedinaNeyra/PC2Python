# Función para ingresar los datos de los alumnos y sus calificaciones
def ingresar_datos_alumnos(n):
    lista_alumnos = []

    for i in range(n):
        alumno = input("Ingrese el nombre del alumno {}: ".format(i + 1))
        nota1 = float(input("Ingrese la primera calificación de {}: ".format(alumno)))
        nota2 = float(input("Ingrese la segunda calificación de {}: ".format(alumno)))
        nota3 = float(input("Ingrese la tercera calificación de {}: ".format(alumno)))

        # Crear un diccionario para almacenar los datos del alumno
        datos_alumno = {
            "Alumno": alumno,
            "Notas": [nota1, nota2, nota3]
        }

        # Agregar el diccionario a la lista de alumnos
        lista_alumnos.append(datos_alumno)

    return lista_alumnos

# Función para mostrar el listado completo de los alumnos y sus calificaciones
def mostrar_listado_alumnos(lista_alumnos):
    print("\nListado de Alumnos:")
    for alumno in lista_alumnos:
        print("Alumno:", alumno["Alumno"])
        print("Notas:", alumno["Notas"])
        print()

# Obtener la cantidad de alumnos
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Llamar a la función para ingresar los datos de los alumnos
alumnos = ingresar_datos_alumnos(num_alumnos)

# Llamar a la función para mostrar el listado completo de los alumnos
mostrar_listado_alumnos(alumnos)
