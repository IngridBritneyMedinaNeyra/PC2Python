def convertir_fecha_numeros(fecha):
    # Separar la fecha en sus componentes (mes, día, año)
    mes, dia, año = map(int, fecha.split('/'))
    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = f"{año:04d}-{mes:02d}-{dia:02d}"
    return fecha_formateada

def convertir_fecha_palabras(fecha):
    # Lista de nombres de meses en español
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    # Separar la fecha en sus componentes (mes, día, año)
    partes = fecha.split()
    mes = partes[0]
    dia = int(partes[1].replace(',', ''))
    año = int(partes[2])
    
    # Convertir el nombre del mes a su número correspondiente
    mes_numero = meses.index(mes) + 1
    
    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = f"{año:04d}-{mes_numero:02d}-{dia:02d}"
    
    return fecha_formateada

# Solicitar al usuario que ingrese una fecha
fecha_usuario = input("Ingrese una fecha (en formato mes/día/año o Mes Día, Año): ")

# Verificar si la fecha está en formato "mes-día-año" o "Mes Día, Año" y llamar a la función correspondiente
if '/' in fecha_usuario:
    fecha_formateada = convertir_fecha_numeros(fecha_usuario)
else:
    fecha_formateada = convertir_fecha_palabras(fecha_usuario)

# Mostrar el resultado
print("Fecha en formato AAAA-MM-DD:", fecha_formateada)
