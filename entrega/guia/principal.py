print ("Taller de AIpython PI E2")
print ("Práctica","en","clase")
print ("Hola",sep="", end="\n")
print ("Hola","Gato", sep="°",end="\n")
print (2*4 + (3*8))
primer_nombre= 'Valeria'
apellido_paterno='Centurión'
print(primer_nombre, apellido_paterno)
print("Usando la funcion print(), "*3)
print(10, 3.14, "Cadena", True)
"""edad = int(input("_Ingrese su edad: "))
print ("Su edad es: ", edad) ## solucion 1
print ("Su edad es: " + str(edad)) ## solucion 2
print (F"Su edad es: {edad}") ## solucion 3 """


num1 = 4
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}") ##Operación dentro del String
texto  = "EsTo eS uN texTo MeZcladO"
## tittle
print(texto.title())
##upper y lower
print (texto.upper())
print (texto.lower())
print (texto.replace(" ", "😃"))
print (len(texto))

def votante ():
    edad = int(input("ingrese su edad: "))
    if( edad >= 18):
        return "Usted debe votar"
    else:
        return "Usted es menor de 18 años."
print(votante())

def vot(edad):
    if(edad >= 18):
        return "Debe votar."
    else:
        return "No puede votar."
    
edad = int(input("ingrese su edad: "))
print(vot(edad))
