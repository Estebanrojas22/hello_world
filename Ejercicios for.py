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

#ejercicio_calcular_edad()

def numeros_impares ():
    numero= int(input("Ingrese el numero: "))

    for i in range(1, numero+1, 2):
        print (i, end="\n")
        time.sleep(1)
        if i==15:
            break;

#numeros_impares()

def reloj_segundos():

    segundos= 60
    cantidad_seg= int(input("Ingrese el limite de segundos: "))
    for i in range(1, segundos+1):
        #time.sleep(1)
        print(i,"seg", end="\n")
        if i== cantidad_seg:
            break;
    print("\33[43m"+"Tiempo terminado"+"\33[0m")

#reloj_segundos()

def interes_anual():
    pesos_año= float(input("Cuanto dinero al año: "))
    tasa_interes= float(input("Tasa de interés anual: "))
    cantidad_años= int(input("Cuantos años: "))
    for i in range(1, cantidad_años+1):
        interes= pesos_año * (tasa_interes/100)
        pesos_año= pesos_año + interes
        print(f"En el año {i}, el dinero acumulado es: ${pesos_año:.2f}")
        time.sleep(1)

#interes_anual()

#def numero_triangulos():
    #numero= int(input("Ingrese un numero: "))
    #for i in range(1, numero+1):
           # print(" " * (numero-i)+ "*" *(1 * i - 1)" " * "*" *(1 * i - 1))
            #time.sleep(1)
   # print("\33[43m"+"Triángulo generado exitosamente"+"\33[0m")
    

#numero_triangulos()    

#def descubrir_contraseña():
    contraseña= "123456"
    contraseña_ingresada=""
    intentos = int(input("Ingrese el numero de intentos: "))
    intento_contador= 1
    while contraseña_ingresada!= contraseña:
        contraseña_ingresada= str(input("Ingrese la contraseña: "))
        print("Contraseña incorrecta, intente nuevamente")
        if intento_contador == intentos:
            print("Se ha superado el numero de intentos")
            break
        intento_contador = intento_contador + 1
        print(contraseña_ingresada = contraseña == "La contrasea es correcta" or contraseña_ingresada != contraseña == "La contraseña es incorrecta")
        
#descubrir_contraseña()


#def contador_caracteres():
    palabra= str(input("Ingrese una frase: "))
    letra= str(input("ingrese la letra que desee contar: "))
    contador= palabra.count(letra)
    print ("La cantidad de letras en la palabra",palabra,"es: ",contador)

#contador_caracteres()

#def contador_letras():
    palabra= str(input("Ingrese una palabra: "))
    letra= str(input("ingrese la letra que desee contar: "))
    contador= 0
    for i in palabra:
        if i == letra:
            contador += 1
    print ("La cantidad de letras en la frase",palabra,"es: ",contador)

#contador_letras()



       
