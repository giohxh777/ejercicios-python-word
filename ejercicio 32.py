#*******area de un rectangulo*******
#******** zona de funciones *************
def capturar_dimensiones():
    largo = float(input("Digite el largo del rectangulo: "))
    ancho = float(input("Digite el ancho del rectangulo: "))
    return largo, ancho
def calcular_area(largo, ancho):
    area = largo * ancho
    return area
def hacer_mensaje(area):
    mensaje = "El area del rectangulo es: " + str(area)
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
largo, ancho = capturar_dimensiones()
area = calcular_area(largo, ancho)
mensaje = hacer_mensaje(area)
imprimir_mensaje(mensaje)
