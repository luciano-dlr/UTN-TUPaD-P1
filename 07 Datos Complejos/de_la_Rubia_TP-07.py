# 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450,
    'Naranja': 1200, 
    'Manzana': 1500, 
    'Pera': 2300
}

precios_frutas['Banana'] = 1330   
precios_frutas['Manzana'] = 1700   
precios_frutas['Melón'] = 2800    


print(precios_frutas)

# 3
precios_frutas = {
    'Banana': 1330, 
    'Ananá': 2500, 
    'Melón': 2800, 
    'Uva': 1450,
    'Naranja': 1200, 
    'Manzana': 1700, 
    'Pera': 2300
}

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# 4
contactos = {}

print("Ingrese 5 contactos (nombre y teléfono):")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ").strip().lower()
    telefono = input(f"Teléfono de {nombre}: ").strip()
    contactos[nombre] = telefono 


print("\n--- Consulta de contactos ---")
consulta = input("Ingrese un nombre para buscar su teléfono: ").strip().lower()


if consulta in contactos:
    print(f"El teléfono de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}'.")

# 5
frase = input("Ingrese una frase: ").strip()

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("\n--- Resultados ---")
print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)

# 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip().title()
    notas = []
    
    for j in range(3):
        while True:
            try:
                nota = input(f"Ingrese la nota {j+1} de {nombre}: ").strip()
                if not nota:  
                    raise ValueError("No puede estar vacío")
                
                nota = float(nota)
                if nota < 0 or nota > 10:  
                    raise ValueError("La nota debe estar entre 0 y 10")
                
                notas.append(nota)
                break
                
            except ValueError as e:
                print(f"Error: {e}. Intente nuevamente.")

    alumnos[nombre] = tuple(notas)

print("\n--- Promedios ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {notas} → Promedio = {promedio:.2f}")
    

# 7
aprobados_parcial1 = {"Juan", "María", "Pedro", "Ana", "Luis"}
aprobados_parcial2 = {"María", "Luis", "Carlos", "Sofía", "Ana"}

ambos_parciales = aprobados_parcial1 & aprobados_parcial2
print("Aprobados en ambos parciales:", ambos_parciales)

solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Aprobados solo en un parcial:", solo_uno)

total_aprobados = aprobados_parcial1 | aprobados_parcial2
print("Total de aprobados (al menos uno):", total_aprobados)

# 8
stock = {
    "Manzanas": 50,
    "Bananas": 30,
    "Leche": 20,
    "Pan": 15
}

def mostrar_menu():
    print("\n--- GESTIÓN DE STOCK MENU---")
    print("1. Consultar stock de un producto")
    print("2. Modificar/Añadir stock")
    print("3. Salir")

def consultar_stock():
    producto = input("Ingrese el nombre del producto: ").strip().title()
    if producto in stock:
        print(f"\n--- Stock de {producto}: {stock[producto]} unidades ---")
    else:
        print(f"El producto '{producto}' no existe en el inventario.")

def modificar_stock():
    producto = input("Ingrese el nombre del producto: ").strip().title()
    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]} unidades")
        try:
            unidades = int(input("Ingrese las unidades a añadir (use negativo para restar): "))
            stock[producto] += unidades
            print(f"Nuevo stock de {producto}: {stock[producto]} unidades")
        except ValueError:
            print("Error: Ingrese un número válido.")
    else:
        print(f"El producto '{producto}' no existe. ¿Desea añadirlo?")
        respuesta = input("S/N: ").strip().lower()
        if respuesta == "s":
            try:
                unidades = int(input("Ingrese el stock inicial: "))
                stock[producto] = unidades
                print(f"Producto '{producto}' añadido con {unidades} unidades.")
            except ValueError:
                print("Error: Ingrese un número válido.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-3): ").strip()
    
    if opcion == "1":
        consultar_stock()
    elif opcion == "2":
        modificar_stock()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")



# 9
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Entrenamiento"
}

def consultar_evento():
    print("\n--- CONSULTAR EVENTO ---")
    dia = input("Ingrese el día (ej: lunes): ").strip().lower()
    hora = input("Ingrese la hora (ej: 10:00): ").strip()
    
    clave = (dia, hora)
    if clave in agenda:
        print(f"\n--- Evento: {agenda[clave]} ---")
    else:
        print("No hay eventos programados para ese día y hora.")

while True:
    print("\n--- AGENDA ---")
    print("1. Consultar evento")
    print("2. Salir")
    opcion = input("Seleccione una opción (1-2): ").strip()
    
    if opcion == "1":
        consultar_evento()
    elif opcion == "2":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

# 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "España": "Madrid"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario original:", paises_capitales)
print("Diccionario invertido:", capitales_paises)