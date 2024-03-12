# Ejercicio 1
num = 0
while (num <= 100):
    print(num)
    num = num + 1

# Ejercicio 2 
for num in range(0,101):
    print(num, end=" ")
print(" ")
# Ejercicio 3
num = 10
while (num >= 0):
    print (num)
    num = num - 1

for num in range(10,-1,-1):
    print(num, end=" ")
print(" ")
# Ejercicio 4
num1 = int(input("Ingrese un número porfavor..."))
num2 = int(input("Ingrese otro número porfavor..."))
while(num1 == num2):
    print("Debe ingresar dos números diferentes.")
    num1 = int(input("Ingrese un número porfavor..."))
    num2 = int(input("Ingrese otro número porfavor..."))
# Fase comparativa (buscar el mayor)
if (num1 > num2):
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

for i in range(menor + 1, mayor):
    print(i,end=", ")
print("")

# Ejercicio 5

numeral = "#"
for i in range (0,7):
    print(numeral)
    numeral = numeral + "#"
print(" ")

# Ejercicio 6
numeral = "#"
for i in range(0,8):
    for x in range(0,7):
        numeral = numeral + "#"
    print(numeral)
    numeral = "#"

# Ejercicio 7
numero = int(input("Ingrese un número: "))
nombre = str(input("Ingrese su nombre: "))

for i in range(0,numero):
    print(nombre)

# Ejercicio 8
numero = int(input("Ingrese un numero mayor a 3: "))
while(numero <= 3):
    print("Debe ingresar un numero mayor a 3")
    numero = int(input("Ingrese un numero mayor a 3: "))
print(F"Números impares que le preceden a {numero}")
for x in range(0,numero):
    if(x % 2 != 0):
        print(x, end=" ")

# Ejercicio 9
print(" ")
for i in range(0,11):
    multiplicacion = i * i
    print(F"{i} x {i} = {multiplicacion}")

# Ejercicio 10
for i in range(0,7):
    for x in range(0,7):
        print(i,x)

# Ejercicio 11
numero_natural = int(input("Ingrese un numero natural: "))
while(numero < 1):
    print("Error, debe ser un numero natural")
    numero_natural = int(input("Ingrese un numero natural: "))

# Ejericio 12
suma = 0
for x in range (0,numero_natural):
    suma = suma + (x+1)
print (suma)

# Ejercicio 13
numero_n = int(input("Ingrese un numero natural: "))
suma_n = 0
for i in range (0,numero_n):
    if(i % 2 == 0):
        suma_n = suma_n + i
print (suma_n)

#Ejercicio 14