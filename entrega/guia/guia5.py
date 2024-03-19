#Ejercicio 1
elementos = list()
#Ejercicio 2
elementos = [1,2,3,4,5,'Helado','Gato']
#Ejercicio 3
print(len(elementos))
#Ejercicio 4
frutas = ['Sandia','Pera','Banana','Frutilla','Durazno','Melón']
# a)
print(len(frutas))
# b)
frutas.remove(frutas[0])
print(frutas)
# c)
frutas.append('Arandanos')
print(frutas)
# Ejercicio 5
tope = len(frutas)
mit = len(frutas) / 2
print(frutas[0], frutas[tope-1])
# Ejercicio 6
datos_personales= ['Valeria',21,1.55,'Soltero','Calle']
# Ejercicio 7
# a)
companias=['Youtube','Spotify','Instagram']
for nombre in companias:
    print(nombre)
# b)
for i in range(len(companias)):
    print(F" Indice: {i} , nombre de la compañia: {companias[i]}")
# c)
companias[2] = 'Discord'
for nombre in companias:
    print(nombre)

# Ejercicio 8
numeros = []
for i in range(1,10):
    numeros.append(i)
print(numeros)
sub_numeros = numeros[:3]
print(sub_numeros)

# Ejercicio 9
letras = ['a','b','c','d','e','f','g','h','i','j']
sub_letra = letras[::2]
print(sub_letra)

# Ejercicio 10
animales = ['Gato','Perro','Pajaro','Leon']
inversa = animales[::-1] 
print(inversa)

# Ejercicio 11
palabras = ['Amapola','Mate','Buen dia','Chau']
sub_lista = palabras[1:4]
print(sub_lista)

# Ejercicio 12
# a)
flores= ['rosas', 'orquídea','lirio','tulipan', 'margarita', 'dalia', 'hortensia']
tres = flores[2:3]
print(tres)

# b)
for i in range (1, len(flores),2):
    print(flores[i])

# c)
print(flores[::3])  

# Ejercicio 13
def caracteres(lista):
    cont = 0
    vocales = "aeiou"
    for char in carac:
        if char in vocales:
            cont = cont + 1
    return cont
carac = ['a','b','c','r','o']
print(caracteres(carac))

# Ejercicio 14
def dos_listas(lista1,lista2):
    lista_nueva = []
    for i in lista1:
        if i not in lista_nueva:
            lista_nueva.append(i)        
        for x in lista2:
            if x not in lista_nueva:
                lista_nueva.append(x)
    return lista_nueva
list1 = ['Chau','Hola']
list2 = ['Pajaro','Gato','Cuatro']
print(dos_listas(list1,list2))

# Ejercicio 15
def promedio(lista_numeros):
    suma = 0
    cant = 0
    for numero in lista_numeros:
        suma = suma + numero
        cant = cant + 1
    return suma/cant

numeros = [1,3,5,66,7,89]
print(promedio(numeros))