#******area cuadrado ******
#*******zona de funciones ********
def capturar_lado ():
    lado = int(input("digite el valor del lado: "))
    return lado

def hacer_area(lado):
    area= (lado * lado)
    return area

def hacer_mesaje(area ):
    mensaje = "la area del cuadrado es: " + str(area)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****

lado = capturar_lado()
area = hacer_area(lado)
mensaje = hacer_mesaje(area)
imprimir_mensaje(mensaje)


    
