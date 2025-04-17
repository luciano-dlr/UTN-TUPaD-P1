#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_ingresada = input("Ingrese su edad porfavor: ")
edad = int(edad_ingresada)

if edad < 0:
    print("Edad no válida")
elif edad < 18:
    print("Es menor de edad")
elif edad < 65:
    print("Es adulto")
else:
    print("Es adulto mayor")
    
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota_ingresada = input("Ingrese su nota porfavor: ")
nota = int(nota_ingresada)

if nota >= 6:
    print("“Aprobado”")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero_ingresad = input("Ingrese un Numero porfavor: ")
numero = int(numero_ingresad)

if numero % 2 == 0 :
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad por favor: "))

if edad < 0:
    print("Edad no válida")
elif edad >= 0 and edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contrasena = (input("Ingrese su contraseña por favor: "))

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 

# 6) escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import median, mean
from collections import Counter

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)


frecuencias = Counter(numeros_aleatorios)
max_frecuencia = max(frecuencias.values())
modas = [num for num, freq in frecuencias.items() if freq == max_frecuencia]

if len(modas) > 1:
    sesgo = "No se puede determinar el sesgo (no hay moda única)"
    moda = "Múltiples modas: " + str(modas)
else:
    #acceder al primer elemento 
    moda = modas[0]
  
    if media > mediana and mediana > moda:
        sesgo = "Sesgo positivo o a la derecha"
    elif media < mediana and mediana < moda:
        sesgo = "Sesgo negativo o a la izquierda"
    elif media == mediana == moda:
        sesgo = "Sin sesgo (distribución simétrica)"
    else:
        sesgo = "Relación no estándar entre media, mediana y moda"

print("\n=== Análisis Estadístico ===")
print(f"Lista generada (primeros 10): {numeros_aleatorios[:10]}...")
print(f"\nMedidas estadísticas:")
print(f"- Media: {media:.2f}")
print(f"- Mediana: {mediana}")
print(f"- Moda: {moda}")
print(f"\nConclusión: {sesgo}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.


texto = input("Ingrese una frase o palabra: ")

ultimo_caracter = texto[-1].lower() if texto else ''

if ultimo_caracter in {'a', 'e', 'i', 'o', 'u'}:
    print(texto + "!")
else:
    print(texto)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:

nombre = input("Ingrese su nombre: ")
opcion = input("Elija 1 (MAYÚS), 2 (minús) o 3 (Primera mayúsc): ")

if opcion == '1':
    print(nombre.upper())
elif opcion == '2':
    print(nombre.lower())
else:
    print(nombre.title())

# 9)

magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))


if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10) 

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == 'N':
        estacion = "invierno"
    else:
        estacion = "verano"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == 'N':
        estacion = "primavera"
    else:
        estacion = "otoño"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == 'N':
        estacion = "verano"
    else:
        estacion = "invierno"
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == 'N':
        estacion = "otoño"
    else:
        estacion = "primavera"
else:
    estacion = "fecha no válida"

print(f"Actualmente es {estacion} en el hemisferio {'norte' if hemisferio == 'N' else 'sur'}.")