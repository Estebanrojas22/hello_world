def suma_dos_valores(sumando1,sumando2):
    global resultado
    resultado = sumando1 + sumando2
    return resultado

#suma_dos_valores(4,5)
#print ("primera suma")
#print (resultado)
#suma_dos_valores(1,2)
#print ("segunda suma")
#print (resultado)


#calculadora suma, resta, multiplicacion, division
def calculadora_dos_valores (numero1,numero2,operador):
    global resultado
    if operador == 1: #si el operador es 1 es suma
        resultado = numero1 + numero2
    elif operador == 2: #si el operador es 2 es resta
        resultado = numero1 - numero2
    elif operador == 3: #si el operador es 3 es multiplicacion
        resultado = numero1 * numero2
    elif operador == 4: #si el operador es 3 es division
        if numero2 == 0:
            print("Error: Division por cero")
        else:
            resultado = numero1 / numero2
    return resultado

#calculadora_dos_valores(1,2,1)
#print ("Suma:",resultado)
#calculadora_dos_valores(10,5,2)
#print ("Resta:",resultado)
#calculadora_dos_valores(4,5,3)
#print ("Multiplicacion:",resultado)
#calculadora_dos_valores(7,6,4)
#print ("Division:",resultado)


#teorema piatagoras

def teorema_piatagoras(cateto1,cateto2):
    global hipotenusa
    hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
    return hipotenusa

#teorema_piatagoras(3,4)
#print ("Hipotenusa:",hipotenusa)

#DESPEJE X

def despeje_x():
    global x
    b= int(input("ingrese el valor de c: "))
    c= int(input("ingrese el valor de b: "))
    x= (c-b)/2
    print("el valor de x es : ",x)
    return x

#despeje_x()

#funcion and

def funcion_and():
    global resultado
    a= bool(input("ingrese el valor de a: "))
    b= bool(input("ingrese el valor de b: "))
    c= bool(input("ingrese el valor de c: "))
    
    resultado=a and b and c
    print ("El resultado es: ",resultado)
    return resultado
#funcion_and()

def pitagoras_funcion_sumar ():
    global resul_pitagoras
    a= int(input("ingrese el valor de a: "))
    b= int(input("ingrese el valor de b: "))
    a2= a**2
    b2= a**2
    suma= suma_dos_valores(a2,b2)
    resul_pitagoras = suma**0.5
    print ("El valor de pitagoras: ",resul_pitagoras)
    return resul_pitagoras

#pitagoras_funcion_sumar()


    #global contador
    #palabra= str(input("Ingrese una palabra: "))
    #letra= str(input("ingrese la letra que desee contar: "))
    #contador= palabra.count(letra)
    #print ("La cantidad de letras en la palabra",palabra,"es: ",contador)
    #return contador

#contador_letras()

def contador_letras ():
    global contador
    palabra= str(input("Ingrese una palabra: "))
    letra= str(input("ingrese la letra que desee contar: "))
    contador= palabra.count(letra)
    print ("La cantidad de letras",letra,"en la palabra",palabra,"es: ",contador)
    print ("La cantidad de letras de la palabra es: ",len(palabra))
    print ("Palabra separada por letras: ",list(palabra))
    return contador

#contador_letras()
import random
def juego_piedra_papel_tijera ():
    jugador1= random.choice (['piedra', 'papel', 'tijera'])
    print (jugador1)
    jugador2= random.choice (['piedra', 'papel', 'tijera'])
    print (jugador2)
    
    if jugador1 == jugador2:
        print ("Jugador 1 saco"" '",jugador1,"' ""Jugador 2 saco",jugador2)
        print ("Empate")
    elif (jugador1 == 'piedra' and jugador2 == 'tijera') or (jugador1 == 'papel' and jugador2 == 'piedra') or (jugador1 == 'tijera' and jugador2 == 'papel'):
        print ("Jugador 1 saco"" '",jugador1,"' ""Jugador 2 saco",jugador2)
        print ("Jugador 1 gana")
    elif (jugador1 == 'tijera' and jugador2 =='papel'):
        print ("Jugador 1 saco"" '",jugador1,"' ""Jugador 2 saco",jugador2)
        print ("Jugador 1 gana")
    elif (jugador1 == 'papel' and jugador2 == 'tijera'):
        print ("Jugador 1 saco"" '",jugador1,"' ""Jugador 2 saco",jugador2)
        print ("Jugador 1 gana")
    else: 
        print ("Jugador 1 saco"" '",jugador1,"' ""Jugador 2 saco",jugador2)
        print ("Jugador 2 gana")
    return

juego_piedra_papel_tijera()