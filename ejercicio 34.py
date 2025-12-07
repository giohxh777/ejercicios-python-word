#********precio del articulo y calcule el 10€% de descuento****
#******** zona de funciones *************
def capturar_precio():
    precio = float(input("Digite el precio del articulo: "))
    return precio
def calcular_descuento(precio):
    descuento = precio * 0.10
    return descuento
def hacer_mensaje(descuento):
    mensaje = "El descuento es de: " + str(round(descuento, 2)) + " euros"
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
precio = capturar_precio()
descuento = calcular_descuento(precio)
mensaje = hacer_mensaje(descuento)
imprimir_mensaje(mensaje)
