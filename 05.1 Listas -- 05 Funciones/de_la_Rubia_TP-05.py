#1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("Por favor ingresa tus datos:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")


informacion_personal(nombre, apellido, edad, residencia)

#4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo con radio {radio} es: {area:.2f}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")

#5
def segundos_a_horas_minutos(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segundos_restantes = resto % 60
    return horas, minutos, segundos_restantes

seg = int(input("Ingrese segundos: "))
h, m, s = segundos_a_horas_minutos(seg)
print(f"{seg} segundos = {h}h {m}m {s}s")

#6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
tabla_multiplicar(numero)

#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)


print("\nResultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print("Calculadora de IMC (Índice de Masa Corporal)")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"\nSu IMC es: {imc}")

#9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatura en Celsius: "))
print(f"Equivalente en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")

#10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

print("Calculadora de promedio de tres números")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
    
promedio = calcular_promedio(num1, num2, num3)
    
print(f"\nEl promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

print("Error: Por favor ingrese números válidos")