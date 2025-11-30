#*********volumen de un cilindro*********
#*********zona de funciones************

def definir_radio () :
    radio = int(input("digite el valor del radio:"))
    return radio

def definir_altura ():
    altura = int(input("digite el valor de la altura:")) 
    return altura

def definir_volumen (radio,altura) :
    volumen = (3.1416 * radio**2 * altura )  
    return volumen

def hacer_mensaje (volumen):
    mensaje = "el volumen de una esfera es: " + str(volumen)
    return mensaje


def imprimir_mensaje (mensaje):
    print(mensaje)
    
    
#*******codigo principal********
    radio = definir_radio()
    altura = definir_altura()
    volumen = definir_volumen(radio, altura)
    mensaje = hacer_mensaje(volumen)
    imprimir = imprimir_mensaje(mensaje)