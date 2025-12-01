#*****pulgadas a centimetros*****
#*****zona funcional*****


def capturar_pulgadas():
    pulgadas = int(input("digite el valor de las pulgadas que desea convertir: ")) 
    return pulgadas

def hacer_convercion(pulgadas):
    conversion= (pulgadas *2.54 )
    return conversion

def hacer_mesaje(pulgadas, conversion ):
    mensaje = str(pulgadas) + " pulgadas convertidas a millas es: " + str(conversion)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****
pulgadas = capturar_pulgadas()
conversion = hacer_convercion(pulgadas)
mensaje = hacer_mesaje(pulgadas, conversion)
imprimir = imprimir_mensaje(mensaje)