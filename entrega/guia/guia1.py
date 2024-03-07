from sympy import false

## Ejercicio 1
print ("Las máquinas me sorprenden con mucha frecuencia")
print ()
print ("tus propios mensajes")
print(23)
print("23")
print("Una computadora puede ser llamada ",'"inteligente"',"si logra engañar a una persona haciéndole creer que es un humano.")
print("Una computadora puede ser llamada \"inteligente\" si logra engañar a una persona haciéndole creer que es un humano.")
print ("Valeria", "Centurión", 21)
print ("Valeria", "Centurion",21, sep="_")
print ("Calle","número","código", sep="\t")
print ("\n","Calle","\n","número","\n","código")
print ("Feliz","\n","Primavera","\n","\t","2024", sep="\t")
print ("Solo podemos ver poco del futuro", end=", ")
print ("pero lo suficiente para darnos cuenta de que hay mucho que hacer")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
## Ejercicio 3
nombre = "Valeria"
apellido = "Centurión"
edad = 21
altura = 1.5
num_vuelo = 2345
temp_ambiente = 18
end_game = "end"
par = false
## Ejercicio 5
nom = str(input("Ingrese su nombre: "))
apell = str(input("Ingrese su apellido: "))
ed = int(input("Ingrese su edad"))
print("Nombre ", nom, " apellido ", apell, " edad: ", ed)
## Ejercicio 6
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
print("suma ", num1 + num2)
print("resta ", num1 - num2)
print("producto ", num1*num2)
print("potencia ", num1**num2)
print("resto ", num1%num2)
num3 = int(input("ingrese un numero: "))
num4 = float(input("ingrese otro numero decimal: "))
print("suma ", num1 + num2)
print("resta ", num1 - num2)
print("producto ", num1*num2)
print("potencia ", num1**num2)
print("resto ", num1%num2)
## Ejercicio 8
base = float(input("Ingrese la base del rectángulo"))
altura = float(input("Ingrese la altura del rectángulo"))
print("área del rectángulo: ", base * altura)
print("perímetro del rectángulo: ", 2*(base + altura))

radio = float(input("ingresa el radio del circulo: "))
area = 3.1416 * radio
print ("la circunferencia es: ", area)

## Ejercicio 9
peso = float(input("ingrese su peso(kg)"))
estatura = float(input("ingrese su estatura(en metros)"))
imc = peso / (estatura**2)
print ("Tu indice de masa corporal es: <", imc, ">")

## Ejercicio 10
grados = int(input("Ingrese un numero (grados celsius)"))
gradosFar = (1.8 * grados) + 32
print ("Los grados celsius: ", grados, " fueron convertidos a Fahrenheit: ", gradosFar)
## Ejercicio 11
h_trabajadas = float(input("Ingrese el número de horas trabajadas"))
costo_hora = float(input("Ingrese el costo por hora"))
print("El sueldo correspondiente es: ", h_trabajadas * costo_hora)

## Ejercicio 12
cant_invertida = float(input("Ingrese la cantidad a invertir"))
int_anual = float(input("Ingresar interés anual"))
anios = int(input("Ingrese el número de años: "))
int_decimal = int_anual / 100
cap_obtenido = cant_invertida * (1 + int_decimal) ** anios

print ("El capital obtenido es: ", cap_obtenido)

## Ejercicio 13
## Ejercicio 14
print('Una ambiciosa' + "introducción " + "a Python")
## Ejercicio 15
sociedad = "aiPython P1"
## a) 
print(sociedad)
## b)
print(len(sociedad))
## c)
print(sociedad.upper())
## d)
print(sociedad.lower())
## Ejercicio 16
texto = "sometimes it is the people no one imagines anything of who do the things that no one can imagine."
print("método capitalize(): "+ texto.capitalize())
print("método title: " + texto.title())
print("método swapcase: ", texto.swapcase())

## Ejercicio 17
nombre_completo = str(input("Ingrese su nombre completo"))
print (nombre_completo * 3)
## Ejercicio 18
espacio = " "
print(F"    {espacio}*")
print(F"   * {espacio} *")
print(F"  *  {espacio}  *")
print(F" *   {espacio}   *")
print(F"***  {espacio}  ***")
print(F"  *  {espacio}  *")
print(F"  *  {espacio}  *")
print(F"  {espacio}*****")



## Ejercicio 19
print ("\n","    *","\n","   * *","\n","  *   *","\n"," *     *","\n","***   ***","\n","  *   *","\n","  *   *","\n","  *****", "\n")

## Ejercicio 20
arbol1 = ("        *\n       * *\n      *   *\n     *     *\n    ***   ***\n      *   *\n      *   *\n      ***** \n")
arbol2 = ("          *\n         * *\n        *   *\n       *     *\n      ***   ***\n        *   *\n        *   *\n        *****")

arboles = arbol1 + "" + arbol2
print(arboles)
 
 ##Ejercicio 21

palabra = str(input("Ingrese una palabra: "))
pal = palabra.replace("a","😃")
print(pal)

## Ejercicio 22 Consultar
oracion = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
dos_primeras_palabras = oracion[0:15]
print(dos_primeras_palabras)

## Ejercicio 23
frase1  = " La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
print(frase1.strip())

## Ejercicio 24
frase = "El razonamiento matemático puede considerarse más bien esquemáticamente \n como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
print(frase)

##Ejercicio 25
separados = "Nombre \t Edad \t Pais \t Ciudad \t\n Alexa \t 250 \t USA \t CapeCod"
print (separados)