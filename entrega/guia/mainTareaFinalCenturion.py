###### Menú ######
from tareaFinalCenturion import *
lanzamiento = 0
lanzamientos_prom = 0
## OPCION MENÚ CON WHILE 
op = True
while op == True:
    print ("*** MENÚ PRINCIPAL ***")
    print ("1. Tirada Simple")
    print ("2. Tirada Múltiple")
    print ("3. Estadísticas")
    print ("Oprima otra tecla para >> Finalizar")
    opc = input("Ingrese una opción ")
    if opc =="1":
        lanzamiento = lanzamiento + 1
        print("Usted ha seleccionado la opción 1: Tirada Simple, debe seleccionar el tipo de dado a lanzar")
        print("Opcion 1: Tetraedro regular, 4 caras.")
        print("Opcion 2: Cubo, 6 caras")
        print("Opcion 3: Octaedro regular, 8 caras")
        print("Opcion 4: Dodecaedro regular, 12 caras")
        print("Opcion 5: Icosaedro regular, 20 caras")
        print("Opcion 6: Trapezoedro pentagonal, 10 caras.")
        op_dado =  int(input("Ingrese el número de la opción de dados a lanzar "))
        cara = 0
        match op_dado:
            case 1:
                cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                print(tiradaSimple(cant_lanzar, cara = 4))
            case 2:
                cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                print(tiradaSimple(cant_lanzar, cara = 6))
            case 3:
                cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                print(tiradaSimple(cant_lanzar, cara = 8))
            case 4:
                cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                print(tiradaSimple(cant_lanzar, cara = 12))
            case 5:
                cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                print(tiradaSimple(cant_lanzar, cara = 20))
            case 6:
                cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                print(tiradaSimple(cant_lanzar, cara = 10))
            case _:
                print("Opción inválida")
    elif opc == "2":
        res = False
        while (res == False):
            lanzamiento = lanzamiento + 1
            print ("Usted ha seleccionado la opcion 2: Tirada Múltiple")
            print("Opcion 1: Tetraedro regular, 4 caras.")
            print("Opcion 2: Cubo, 6 caras")
            print("Opcion 3: Octaedro regular, 8 caras")
            print("Opcion 4: Dodecaedro regular, 12 caras")
            print("Opcion 5: Icosaedro regular, 20 caras")
            print("Opcion 6: Trapezoedro pentagonal, 10 caras.")
            op_dado =  int(input("Ingrese el número de la opción de dados a lanzar "))
            cara = 0
            match op_dado:
                case 1:
                    cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                    print(multi_lanzamiento(cant_lanzar, cara = 4))
                case 2:
                    cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                    print(multi_lanzamiento(cant_lanzar, cara = 6))
                case 3:
                    cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                    print(multi_lanzamiento(cant_lanzar, cara = 8))
                case 4:
                    cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                    print(multi_lanzamiento(cant_lanzar, cara = 12))
                case 5:
                    cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                    print(multi_lanzamiento(cant_lanzar, cara = 20))
                case 6:
                    cant_lanzar = int(input("Ingrese cantidad de dados a lanzar: "))
                    print(multi_lanzamiento(cant_lanzar, cara = 10))
                case _:
                    print("Opción inválida")
            respuesta = str(input("¿Desea seguir lanzando dados? Responder 'Si/No'"))
            respuesta.lower()
            if respuesta == "no":
                res = True
            
    elif opc == "3":
        print("Usted ha seleccionado ver estadisticas")
        print(estadisticas(lanzamiento, lanzamientos_prom))
    else:
        op = False

# La opción del match menú, solo se ejecuta una vez y no en bucle,
# asi que no pude utilizarla, intenté encerrarla en un while pero no funcionó
"""print("Bienvenido al simulador de juego de Dados, elige una opción para comenzar!!..")
print("Opcion 1: Tirada Simple ")
print("Opcion 2: Tirada Múltiple ")
print("Opcion 3: Ver estadísticas ")
print("Oprima otra tecla para salir. ")
op = int(input("Ingrese un número del 1 al 3: "))
match op: