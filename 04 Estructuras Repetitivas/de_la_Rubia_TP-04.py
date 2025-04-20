# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):  
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
contador = 0
if numero == 0:
    contador = 1  
else:
    while numero != 0:
        numero = numero // 10  
        contador += 1
print(f"El número ingresado tiene: {contador} dígitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero_ingresado1 = int(input("Ingrese el primer número: "))
numero_ingresado2 = int(input("Ingrese el segundo número: "))


inicio = min(numero_ingresado1, numero_ingresado2) + 1 
fin = max(numero_ingresado1, numero_ingresado2)         

suma = sum(range(inicio, fin))

print(f"La suma de los números entre {numero_ingresado1} y {numero_ingresado2} (excluyéndolos) es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma_total = 0

while True:
    
    numero_ingresado = int(input("ingrese un numero entero, si desea sumarlos ingrese el valor  0 : "))

    if numero_ingresado == 0:
        break
    suma_total += numero_ingresado
    
print(f"La suma total de los números ingresados es: {suma_total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 

numero_secreto = random.randint(0, 9) 

intentos = 0

print("¡Adivina el número secreto entre 0 y 9!")

while True:
    
    numero_ingresado = int(input("Ingrese un numero Porfavor:"))
    intentos += 1
    
    if  numero_ingresado < numero_secreto:
        print("El número secreto es mayor. ¡Sigue intentando!")
    elif  numero_ingresado > numero_secreto:
        print("El número secreto es menor. ¡Sigue intentando!")
    else:
        print(f"¡Correcto! El número era {numero_secreto}.")
        print(f"Necesitaste { intentos} intentos.")
        break  

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for numero in range(100,-1,-2):  
    print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero_ingresado = int(input("Ingrese un número entero positivo: "))

if numero_ingresado < 0:
    print("¡Error! Debe ingresar un número positivo.")
else:
    suma = sum(range(numero_ingresado + 1)) 
    print(f"La suma de los números desde 0 hasta {numero_ingresado} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)

cantidad_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            numero = int(input(f"Número {i + 1}/{cantidad_numeros}: "))
            break
        except ValueError:
            print("¡Error! Ingrese solo números enteros.")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"- Pares: {pares}")
print(f"- Impares: {impares}")
print(f"- Positivos: {positivos}")
print(f"- Negativos: {negativos}")
print(f"- Ceros: {cantidad_numeros - (positivos + negativos)}")  

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 5  
suma_total = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            numero = int(input(f"Número {i + 1}/{cantidad_numeros}: "))
            break
        except ValueError:
            print("¡Error! Ingrese solo números enteros.")
    suma_total += numero 

media = suma_total / cantidad_numeros  

print("\nResultados:")
print(f"- Media: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_ingresado = input("Ingrese un número entero: ")
numero_invertido = numero_ingresado[::-1] 
print(f"El número invertido es: {numero_invertido}")