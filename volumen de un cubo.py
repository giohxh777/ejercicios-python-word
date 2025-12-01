#******volumen de un cubo******
#*******zona de funciones ********


def capturar_lado ():
    lado = int(input("digite el valor del lado: "))
    return lado

def hacer_volumen(lado):
    volumen= (lado * lado * lado)
    return volumen

def hacer_mesaje(volumen):
    mensaje = "el volumen del cubo es: " + str(volumen)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****
lado = capturar_lado()
volumen = hacer_volumen(lado)
mensaje = hacer_mesaje(volumen)
imprimir = imprimir_mensaje(mensaje)