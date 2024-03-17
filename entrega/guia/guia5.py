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


