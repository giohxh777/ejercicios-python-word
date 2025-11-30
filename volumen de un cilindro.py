#*********volumen de un cilindro*********
#*********zona de funciones************

def definir_radio () :
    radio = float(input("digite el valor del radio:"))
    return radio

def definir_altura ():
    altura = float(input("digite el valor de la altura:")) 
    return altura

def definir_volumen (radio,altura) :
    volumen = float(3.1416 * radio**2 * altura )  
    return volumen

def hacer_mensaje (volumen):
    mensaje = "El volumen del cilindro es: " + str(volumen)
    return mensaje


def imprimir_mensaje (mensaje):
    print(mensaje)
    
    
#*******codigo principal********
def main():
    radio = definir_radio()
    altura = definir_altura()
    volumen = definir_volumen(radio, altura)
    mensaje = hacer_mensaje(volumen)
    imprimir_mensaje(mensaje)

if __name__ == '__main__':
    main()
