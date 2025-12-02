#**********producto de dos numeros**********
#******** zona de funciones *************
def capturar_n1():
    n1 = int(input("digite el valor del numero 1: "))
    return n1

def capturar_n2():
    n2 = int(input("digite el valor del numero 2: "))
    return n2

def hacer_producto(n1,n2):
    producto = n1 * n2
    return producto

def hacer_mensaje(producto):
    mensaje = "el producto de los dos numeros es: " + str(producto)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#******** zona codigo principal ************    
n1 = capturar_n1()
n2 = capturar_n2()
producto = hacer_producto(n1,n2)
mensaje = hacer_mensaje(producto)
imprimir_mensaje(mensaje)
