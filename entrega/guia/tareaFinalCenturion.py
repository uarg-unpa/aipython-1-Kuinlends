import random

def lanza_dado(caras):
    return random.randint(1,caras)

## Variables a utilizar
promedio = 0
minimo = 0
maximo = 0
# Listas a utilizar
dados_tirada_simple = []
resultados_tirada_simple = []
dados_tirada_mult = []
resultados_tirada_mult = []
# Una tirada simple
def tiradaSimple(numero,cara):
    global promedio
    global minimo
    global maximo
    # Guardamos cada dado a lanzar en una lista
    for i in range(0,numero):
        dados_tirada_simple.append(cara)
    #Lanzamos cada dado y guardamos cada resultado 
    for x in range(numero):
        resultados_tirada_simple.append(lanza_dado(dados_tirada_simple[x]))
    # Sumamos los resultados de cada dado para saber el total
    suma = 0
    for res in range(len(resultados_tirada_simple)):
        suma = suma + resultados_tirada_simple[res]
    print("Se muestra los resultados individuales que dieron cada dado al momento de la tirada: ")
    for x in range(len(resultados_tirada_simple)):
        print(resultados_tirada_simple[x], end=" ")
    promedio = promedio + suma
    return F"El resultado total de la suma de los dados tirados fue: {suma}"


def multi_lanzamiento(numero, cara):
    global promedio
    global minimo
    global maximo
    # Guardamos cada dado a lanzar en una lista
    for i in range(0,numero):
        dados_tirada_mult.append(cara)
    #Lanzamos cada dado y guardamos cada resultado 
    for x in range(numero):
        resultados_tirada_mult.append(lanza_dado(dados_tirada_mult[x]))
    # Sumamos los resultados de cada dado para saber el total
    suma = 0
    for res in range(len(resultados_tirada_mult)):
        suma = suma + resultados_tirada_mult[res]
    print("Se muestra los resultados individuales que dieron cada dado al momento de la tirada: ")
    for x in range(len(resultados_tirada_mult)):
        print(resultados_tirada_mult[x], end=" ")
    promedio = promedio + suma
    return F"El resultado total de la suma de los dados tirados fue: {suma}"


def estadisticas(lanzamientos, promedio_lanzamiento):
    if lanzamientos != 0:
        promedio_lanzamiento = (int)(promedio / lanzamientos)
        print(F"El total de lanzamientos realizados fue: {lanzamientos}, el promedio de todos los resultados fue: {promedio_lanzamiento}")
        if(len(resultados_tirada_simple)>0):
            print("Se muestran resultados estadísticos para las tiradas simples")
            minimo = min(resultados_tirada_simple)
            maximo = max(resultados_tirada_simple)
            print("El valor más bajo obtenido fue: ", minimo, " mientras que el valor más alto obtenido fue: ", maximo)
        else:
            print("No se han registrado valores en tiradas simples para obtener estadisticas")
    
        if(len(resultados_tirada_mult)>0):
            print("Se muestran resultados estadísticos para las tiradas múltiples")
            promedio_lanzamiento = (int)(promedio / lanzamientos)
            minimo = min(resultados_tirada_mult)
            maximo = max(resultados_tirada_mult)
            print("El valor más bajo obtenido fue: ", minimo, " mientras que el valor más alto obtenido fue: ", maximo)
        else:
            print("No se han registrado valores en tiradas multiples para obtener estadisticas")
