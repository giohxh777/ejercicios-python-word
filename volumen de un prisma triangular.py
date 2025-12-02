#*****volumen prisma*****
#*****zona funcional*****

def capturar_longitud():
    longitud = int(input("digite el valor de la longitud: ")) 
    return longitud

def capturar_altura():
    altura = int(input("digite el valor de la altura: ")) 
    return altura

def capturar_base():
    base = int(input("digite el valor de la base del prisma: ")) 
    return base

def hacer_volumen(longitud, altura, base):
    volumen = (longitud * altura * base) / 2
    return volumen

def hacer_mesaje(volumen):
    mensaje = "el volumen de un prisma triangular es: " + str(volumen)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****

longitud = capturar_longitud()
altura = capturar_altura()
base = capturar_base()
volumen = hacer_volumen(longitud, altura, base)
mensaje = hacer_mesaje(volumen)
imprimir_mensaje(mensaje)


 