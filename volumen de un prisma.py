#*****volumen prisma*****
#*****zona funcional*****

def capturar_longitud():
    longitud = int(input("digite el valor de la longitud: ")) 
    return longitud

def capturar_ancho():
    ancho = int(input("digite el valor del ancho: ")) 
    return ancho

def capturar_altura():
    altura = int(input("digite el valor de la altura: ")) 
    return altura

def hacer_volumen(longitud, ancho, altura):
    volumen = (longitud * altura * ancho)
    return volumen

def hacer_mesaje(volumen):
    mensaje = "el volumen de un prisma rectangular es: " + str(volumen)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****
def main():
    longitud = capturar_longitud()
    ancho = capturar_ancho()
    altura = capturar_altura()
    volumen = hacer_volumen(longitud, ancho, altura)
    mensaje = hacer_mesaje(volumen)
    imprimir_mensaje(mensaje)

if __name__ == '__main__':
    main()