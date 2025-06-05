#1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))

print("\nFactoriales desde 1 hasta", numero, ":")
for i in range(1, numero + 1):
    print(f"Factorial de {i} es {factorial(i)}")
    
#2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingrese la posición hasta la que desea generar la serie de Fibonacci: "))

print(f"\nSerie de Fibonacci hasta la posición {n}:")
for i in range(n + 1):
    print(f"Posición {i}: {fibonacci(i)}")
    
# 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else :
        return 1 / (base * potencia(base, exponente - 1))

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))

if exponente < 0:
    print("El exponente debe ser un entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"\n{base} elevado a {exponente} es: {resultado}")
    
# 4
def decimal_a_binario_recursivo(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario_recursivo(num // 2) + str(num % 2)
    
num = int(input("Ingresa un numero decimal para convertirlo a binario: "))
print(f"El numero {num} en binario es: {decimal_a_binario_recursivo(num)}")

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra_ingresada = input("Ingrese una Palabra: ").lower()
print(f"Es palíndromo la palabra: {palabra_ingresada}" 
        if es_palindromo(palabra_ingresada)
        else f"No es palíndromo la palabra {palabra_ingresada}")

#6
def sumar_digitos(numero):
    if numero // 10 == 0:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)

def verificar_positivo(numero):
    if numero >= 0:
        return numero
    else:
        print("¡El número debe ser positivo! Intenta nuevamente.")
        return verificar_positivo(int(input("Ingresa un número entero positivo: ")))

numero = int(input("Ingresa un número: "))
numero_verificado = verificar_positivo(numero)
print(f"- La suma de los dígitos de {numero_verificado} es {sumar_digitos(numero_verificado)}")

# 7
def contar_bloques(n):
    if n == 0:
        return 0
    return n + contar_bloques(n - 1)

cantidad_de_bloques_nivel_bajo = int(input("Bloques en el nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(cantidad_de_bloques_nivel_bajo)}")

#8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def verificar_positivo(num):
    if num > 0:
        return num
    print("¡El número debe ser positivo!")
    return verificar_positivo(int(input("Ingresa un número entero positivo: ")))

def verificar_digito(digito):
    if 0 <= digito <= 9:
        return digito
    print("¡El dígito debe estar entre 0 y 9!")
    return verificar_digito(int(input("Ingresa un dígito válido (0-9): ")))


numero = verificar_positivo(int(input("Número: ")))
digito = verificar_digito(int(input("Dígito a contar (0-9): ")))
print(f"Aparece {contar_digito(numero, digito)} veces")

