#1 
multiplos = list(range(4, 101, 4))
print(multiplos)

#2
elemntos = [1,2,3,4,5]
penultimo_neg = elemntos[-2] 
print(penultimo_neg)

#3
lista_vacia = []

lista_vacia.append('cebolla')
lista_vacia.append('tomate')
lista_vacia.append('lechuga')

print('Mi ensalada favorita es : ',lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro" 
animales[-1] = "oso" 

print(animales)

#5
# Primero max(numeros) encuentra el valor máximo de la lista → 22 (el mayor número)
# Luego remove() busca y elimina ese valor (22) de la lista
# El programa elimina el número más grande de la lista original.
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#6
lista = list(range(10, 31, 5)) 
print("Lista completa:", lista)
dos_primeros = lista[0] , lista[1]
print("Los dos primeros:", dos_primeros) 

#7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "nuevo_modelo1"  
autos[2] = "nuevo_modelo2" 

print("Lista actualizada:", autos)

#8
dobles = []

dobles.append(5 * 2)  
dobles.append(10 * 2)  
dobles.append(15 * 2)  

print("Lista de dobles:", dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras[2].append('jugo')
compras[1].remove('fideos')
compras[1].append('tallarines')
compras[0].remove('pan')

print(compras)

#10
lista_anidada = []          
lista_anidada.append(15)     
lista_anidada.append(True)   

sublista = [25.5, 57.9, 30.6] 
lista_anidada.append(sublista) 

lista_anidada.append(False) 

print(lista_anidada)        