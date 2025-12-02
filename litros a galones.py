#***********zona de fiunciones*********
#***********litros a galones************
def capturar_litros():
    litros = int(input("digite el valor de los litros que desea convertir: ")) 
    return litros

def hacer_convercion(litros):
    conversion= (litros*0.264172)
    return conversion

def hacer_mesaje(litros, conversion ):
    mensaje = str(litros) + " litros convertido a galones es: " + str(conversion)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****

litros = capturar_litros()
conversion = hacer_convercion(litros)
mensaje = hacer_mesaje(litros, conversion)
imprimir_mensaje(mensaje)

  