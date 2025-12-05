#************division entre el primero y el segundo numero***********
#******** zona de funciones *************
def capturar_n1():
    n1 = int(input("digite el valor del numero 1: "))
    return n1
def capturar_n2():
    n2 = int(input("digite el valor del numero 2: "))
    return n2
def hacer_division(n1,n2):
    division = n1 / n2
    return division
def hacer_mensaje(division):
    mensaje = "la division del primer numero entre el segundo es: " + str(division)
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
n1 = capturar_n1()
n2 = capturar_n2()
division = hacer_division(n1,n2)
mensaje = hacer_mensaje(division)
imprimir_mensaje(mensaje)
