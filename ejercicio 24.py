#***********producto de dichos valores************
#******** zona de funciones *************

def capturar_numero():
    numero = int(input("Digite un numero: "))
    return numero
def calcular_cuadrado(numero):
    cuadrado = numero * numero
    return cuadrado
def hacer_mensaje(cuadrado):
    mensaje = "El cuadrado del numero es: " + str(cuadrado)
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
numero = capturar_numero()
cuadrado = calcular_cuadrado(numero)
mensaje = hacer_mensaje(cuadrado)
imprimir_mensaje(mensaje)
