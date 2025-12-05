#*******raiz cuadrada utilizando operadores aritmeticos*********
def raiz_cuadrada(numero):
    raiz = numero ** 0.5
    return raiz
def capturar_numero():
    numero = int(input("digite un numero para calcular su raiz cuadrada: "))
    return numero
def hacer_mensaje(raiz):
    mensaje = "la raiz cuadrada del numero es: " + str(raiz)
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
numero = capturar_numero()
raiz = raiz_cuadrada(numero)
mensaje = hacer_mensaje(raiz)
imprimir_mensaje(mensaje)
