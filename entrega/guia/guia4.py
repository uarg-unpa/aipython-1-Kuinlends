# Ejercicio 1
def multiplicacion(num1,num2):
    return num1 * num2

# Ejercicio 2
"""def multiplicacion():
    return 1*1"""

# Ejercicio 3
def mensaje(nombre):
    print ("Su nombre es: ", (str) (nombre))

# Ejercicio 4
def tabla(numero):
    for i in range (1,10):
        multi = i * numero
        print(F" {numero} x {i} = {multi}")

# Ejercicio 5
def parImpar(num):
    if(num % 2 ==0):
        return "Es par"
    else:
        return "Es impar"

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
        print("Todos los numeros ingresados son iguales")

# Ejercicio 8
def invertir(palabra):
    long = palabra.len()
    for i in range (0,long):
        
