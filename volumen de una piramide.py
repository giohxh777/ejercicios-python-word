#*****volumen piramide*****
#*****zona funcional*****

def capturar_longitud():
    longitud = int(input("digite el valor de la longitud de la base: ")) 
    return longitud

def capturar_ancho():
    ancho = int(input("digite el valor del ancho de la base: ")) 
    return ancho

def capturar_altura():
    altura = int(input("digite el valor de la altura: ")) 
    return altura

def hacer_volumen(longitud, ancho, altura):
    volumen = ( 1/3 * longitud * altura * ancho)
    return volumen

def hacer_mesaje(volumen):
    mensaje = "el volumen de una piramide es: " + str(volumen)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****


longitud = capturar_longitud()
ancho = capturar_ancho()
altura = capturar_altura()
volumen = hacer_volumen(longitud, ancho, altura)
mensaje = hacer_mesaje(volumen)
imprimir_mensaje(mensaje)
