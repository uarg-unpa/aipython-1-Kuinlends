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

