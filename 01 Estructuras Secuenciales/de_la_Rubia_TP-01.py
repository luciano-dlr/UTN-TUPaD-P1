# 1
print("Hola Mundo")

# 2
nombre_ingresado = input("Ingrese su nombre porfavor: ")
print(f"Bienvenido {nombre_ingresado} !")

#3
nombre_ingresado = input("Ingrese su nombre porfavor: ")
apellido_ingresado = input("Ingrese su apellido porfavor: ")
edad_ingresada = input("Ingrese su edad porfavor: ")
pais_ingresado = input("Ingrese el pais donde usted vive actualmente porfavor: ")
print(f"Soy {nombre_ingresado} {apellido_ingresado}, tengo {edad_ingresada} años y vivo en {pais_ingresado}")

# 4
radio_ingresado = input("Ingrese la medida del radio para calcular su area y perimetro: " )
radio_ingresado = int(radio_ingresado)
calculo_area = radio_ingresado * 3.14
calculo_perimetro = 2 * 3.14 * radio_ingresado
print(f"El area de su circulo es {calculo_area} y su perimetro {calculo_perimetro}")

#5
segundos_ingresados = input("Ingrese un numero que represente una cantidad de segundos para que el programa indique cantidad de horas que equivale: ")
segundos_ingresados= int(segundos_ingresados)
calculo_horas = segundos_ingresados / 3600
print(f"Equivale a {calculo_horas} horas")

#6
numero_ingresado = input("Ingrese un numero para mostrar sus valores en la tabla: ")
numero_ingresado = int(numero_ingresado)
print(f"Tabla de multiplicar del {numero_ingresado}:")
for i in range(1, 11):
    resultado = numero_ingresado * i
    print(f"{numero_ingresado} x {i} = {resultado}")

#7
numero1_ingresado = input("Ingrese un numero entero porfavor: ")
numero2_ingresado = input("Ingrese otro numero entero porfavor: ")

numero1_ingresado = int(numero1_ingresado)
numero2_ingresado = int(numero2_ingresado)

suma = numero1_ingresado + numero2_ingresado
resta = numero1_ingresado - numero2_ingresado
multiplicacion = numero1_ingresado * numero2_ingresado
division = numero1_ingresado / numero2_ingresado

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# 8
altura_ingresada = input("Ingrese su altura porfavor: ")
peso_ingresado = input("Ingrese su peso en kilogramos porfavor: ")

altura_ingresada = float(altura_ingresada)
peso_ingresado = int(peso_ingresado)

calculo_masa_corporal = peso_ingresado / altura_ingresada ** 2

print(f"Su indice de masa corporall es de {calculo_masa_corporal}")

# 9
temperatura_ingresada = input("Ingrese una temperatura en grados celsius: ")
temperatura_ingresada= float(temperatura_ingresada)
temperatura_fahrenheit = 9/5 * temperatura_ingresada + 32
print(f"La temperatura ingresada celsius, su valor a fahrenheit es: {temperatura_fahrenheit}")

#10
numero1_ingresado = input("Vamos a calcular el promedio de 3 numeros, ingrese el primero: ")
numero2_ingresado = input("Ingrese el segundo numero porfavor: ")
numero3_ingresado = input("Ingrese el tercer numero porfavor: ")

numero1_ingresado=float(numero1_ingresado)
numero2_ingresado=float(numero2_ingresado)
numero3_ingresado=float(numero3_ingresado)

calculo_promedio = (numero1_ingresado + numero2_ingresado + numero3_ingresado) / 3

print(f"El promedio de los 3 numeros es: {calculo_promedio}")