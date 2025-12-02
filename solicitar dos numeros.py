#*******solucitar dos numeros********
#********* zona de funciones *************

def capturar_n1():
    n1 = int(input("digite el valor del numero 1: "))
    return n1

def capturar_n2():
    n2 = int(input("digite el valor del numero 2: "))
    return n2

def hacer_suma(n1,n2):
    suma = n1 + n2
    return suma

def hacer_mensaje(suma):
    mensaje = "la suma de los dos numeros es: " + str(suma)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************

n1 = capturar_n1()
n2 = capturar_n2()      
suma = hacer_suma(n1,n2)
mensaje = hacer_mensaje(suma)
imprimir_mensaje(mensaje)



