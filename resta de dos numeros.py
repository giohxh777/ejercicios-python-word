#*********resta de dos numeros*********
#******** zona de funciones *************
def capturar_n1():
    n1 = int(input("digite el valor del numero 1: "))
    return n1

def capturar_n2():
    n2 = int(input("digite el valor del numero 2: "))
    return n2

def hacer_resta(n1,n2):
    resta = n1 - n2
    return resta

def hacer_mensaje(resta):
    mensaje = "la resta de los dos numeros es: " + str(resta)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#******** zona codigo principal ************
n1 = capturar_n1()
n2 = capturar_n2()
resta = hacer_resta(n1,n2)
mensaje = hacer_mensaje(resta)
imprimir_mensaje(mensaje)