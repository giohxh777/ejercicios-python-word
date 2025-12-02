#*****libras a kilogramos*****
#*****zona funcional*****


def capturar_libras():
    libras = int(input("digite el valor de las libras que desea convertir: ")) 
    return libras

def hacer_convercion(libras):
    conversion= (libras *0.453592 )
    return conversion

def hacer_mesaje(libras, conversion ):
    mensaje = str(libras) + " libras convertidas a kilogramos es: " + str(conversion)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****
libras = capturar_libras()
conversion = hacer_convercion(libras)
mensaje = hacer_mesaje(libras, conversion)
imprimir = imprimir_mensaje(mensaje)