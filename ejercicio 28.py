#**********base y altua de un triangulo***********
#******** zona de funciones *************
def capturar_base():
    base = float(input("digite el valor de la base del triangulo: "))
    return base
def capturar_altura():
    altura = float(input("digite el valor de la altura del triangulo: "))
    return altura
def calcular_area(base,altura):
    area = (base * altura) / 2
    return area
def hacer_mensaje(area):
    mensaje = "el area del triangulo es: " + str(area)
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
base = capturar_base()
altura = capturar_altura()
area = calcular_area(base,altura)
mensaje = hacer_mensaje(area)
imprimir_mensaje(mensaje)
