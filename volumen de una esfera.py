#***********zona de funciones***********
#**********volumen esfera***************

def capturar_radio():
    radio= int(input("digitar el radio"))
    return radio 


def digitar_volumen(radio):
    volumen = (4/3 * 3.1416 * radio**3)
    return volumen 


def digitar_mensaje(volumen):
    mensaje = "el volumen de una esfera es :" +str(volumen)
    return mensaje


def imprimir_mensaje(mensaje):
    print(mensaje)
    
#**********zona codigo principal**********

radio= capturar_radio()
volumen = digitar_volumen(radio)
mensaje = digitar_mensaje(volumen)
imprimir = imprimir_mensaje(mensaje)