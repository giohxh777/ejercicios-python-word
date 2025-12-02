#**********area de un circulo*********
#**********zona de funciones**********

def definir_radio():
    radio = float(input("Digite el valor del radio: "))
    return radio
    
def definir_area (radio):
    area = 3.1416 * radio ** 2
    return area
    
def hacer_mensaje (area):
    mensaje = "El área del círculo es: " + str(area)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#*******codigo principal********

radio = definir_radio()
area = definir_area(radio)
mensaje = hacer_mensaje(area)
imprimir_mensaje(mensaje)


