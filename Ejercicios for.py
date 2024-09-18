import time

def ejercicio_1 ():
    palabra= str(input("ingresar palabra: "))
    cantidad= int(input("ingrese la cantidad de veces: "))
    for i in range(cantidad):
        print("valor de la variable i: ", i+1)
        print(palabra)
        time.sleep(1)
    return palabra

#ejercicio_1()

import time

def ejercicio_edad ():
    edad= int(input("ingrese su edad: "))
    for i in range(edad):
        print("edad : ", i+1)
        print(i+1)
        time.sleep(1)
#ejercicio_edad()

def ejercicio_calcular_edad ():
    año_actual= int(input("Ingrese el año actual: "))
    año_nacimiento= int(input("Ingrese el año nacimiento: "))
    edad= año_actual - año_nacimiento
    print("su edad es: ", edad)
    for i in range(edad):
        print(i+1)
        time.sleep(1)
    return edad

ejercicio_calcular_edad()