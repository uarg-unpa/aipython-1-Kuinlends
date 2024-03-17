# Ejercicio 1
def multiplicacion(num1,num2):
    return num1 * num2

# Ejercicio 2
def multiplicacion1(num1=1,num2=1):
    return num1 * num2

# Ejercicio 3
def mensaje(nombre):
    return "¡Que tengas un buen dia Sr/a ", (str) (nombre) , "!" 

# Ejercicio 4
def tabla(numero):
    for i in range (1,10):
        multi = i * numero
        print(F" {numero} x {i} = {multi}")

# Ejercicio 5
def parImpar(num):
    if(num % 2 ==0):
        return F"El numero ingresado: {num}, es par"
    else:
        return F"El numero ingresado: {num}, es impar"

# Ejercicio 6
def factorial(num):
    for x in range(1,num):
        mult = x * num
        print(mult)

# Ejercicio 7
def elMaximo(num1,num2,num3):
    maximo = 0
    if(num1 > num2 and num1 > num3):
        maximo = num1
    elif(num2 > num1 and num2 > num3):
        maximo = num2
    elif(num3 > num1 and num3 > num2):
        maximo = num3
    else:
        return "Todos los numeros ingresados son iguales"
    return F"El maximo de los numeros ingresados fue el {maximo}"

# Ejercicio 8
def invertir(palabra):
    indice = len(palabra) - 1
    palabra_invertida = ""
    while indice >= 0:
        palabra_invertida = palabra_invertida + palabra[indice]
        indice = indice-1
    print(palabra_invertida)
# Ejercicio 9
def palindromo(palabra):
    indice = len(palabra) - 1
    palabra_invertida = ""
    while indice >= 0:
        palabra_invertida = palabra_invertida + palabra[indice]
        indice = indice-1
    palindromo = False
    palabra = palabra.lower()
    palabra_invertida = palabra_invertida.lower()
    for i in range (len(palabra)):
        if palabra[i] == palabra_invertida[i]:
            palindromo = True
        else:
            palindromo = False
    return palindromo

# Ejercicio 10
def temperaturas(temperatura):
    celsius = (temperatura-32) / 1.8
    return F"La temperatura {temperatura} fue convertida a Fahrenheit resultando en: {celsius}"

# Zona de pruebas
#Ej1
print(multiplicacion(6,4))
#Ej2
print(multiplicacion1())
#Ej3
print(mensaje("Valeria"))
#Ej4
tabla(4)
#Ej5
print(parImpar(5))
#Ej6
factorial(8)
#Ej7
print(elMaximo(5,5,5))
#Ej8
invertir("Hola")
#Ej9
print(palindromo("Arenera"))
#Ej10
print(temperaturas(80))
