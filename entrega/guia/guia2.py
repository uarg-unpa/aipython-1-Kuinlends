## Ejercicio 1

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Tiene edad suficiente para conducir")
else:
    aux = 18 - edad
    print("Le faltan ", aux ," años para conducir.")
## Ejercicio 2
edad1= int(input("Ingrese su edad: "))
if edad1 >= 21:
    print("¡¡¡Tenemos la misma edad!!!")
elif (21 - edad1) == 1:
    print("año")
else:
    print("años")

## Ejercicio 3
password = str(input("Ingrese una contraseña para almacenar: "))
login = str(input("Ingrese su contraseña..."))
if ((password.lower()) == (login.lower())):
    print ("Contraseña exitosa")
else: 
    print("Contraseña incorrecta.")

## Ejercicio 4
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
if a > b:
    print("a es mayor que b") 
elif a < b:
    print("a es menor que b")
else:
    print("a es igual que b")
## Ejercicio 5
num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("es par")
else:
    print("es impar")
## Ejercicio 6
numm = int(input("Ingrese un número del 1 al 7: "))
match numm:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _: 
        print ("Opción no válida")

# Ejercicio 7
puntuacion = int(input("Ingrese la puntuacion del estudiante: "))
while (puntuacion < 0) or (puntuacion > 100):
    print("La puntuacion debe ser entre 0 a 100 puntos")
    puntuacion = int(input("Vuelva a ingresar la puntuacion"))

if (puntuacion >= 80) and (puntuacion <=100):
    print ("Clasificación A")
elif (puntuacion >= 70) and (puntuacion <=79):
    print("Clasificacion B")
elif (puntuacion >= 60) and (puntuacion <= 69):
    print("Clasificación C")
elif (puntuacion >= 50) and (puntuacion <= 59):
    print ("Clasificacion D")
else:
    print("Clasificacion F")

# Ejercicio 8
    edad_cliente = int(input("Cliente: Ingrese su edad... "))
    if (edad_cliente < 4):
        print("Menor de 4 años de edad: entra gratis.")
    elif (edad_cliente >= 4) and (edad_cliente <= 18):
        print(" Usted debe pagar $5")
    else:
        print("Usted debe pagar 10$")
# Ejercicio 9
edad_usuario = int(input("Ingrese su edad porfavor: "))
ingr_mensual = int(input("Ingrese sus ingresos mensuales: "))
if (edad_usuario >= 18) and (edad_usuario >= 100000):
    print("Usted debe pagar impuestos.")
else:
    print("Usted se encuentra excento a pagar impuestos.")