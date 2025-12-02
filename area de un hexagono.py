#******area de un hexagono ******
#*******zona de funciones ********
def capturar_parimetro ():
    perimetro = int(input("digite el valor de la perimetro: "))
    return perimetro

def capturar_apotema ():
    apotema = int(input("digite el valor de la apotema: "))
    return apotema

def hacer_area (perimetro, apotema):
    area = (perimetro * apotema ) / 2
    return area

def hacer_mensaje(area):
    mensaje = "la area del hexagono es: " + str(area)
    return mensaje 

def imprimir_mensaje(mensaje):
    print (mensaje)
    
    
#***** zona codigo principal*******

perimetro = capturar_base()
apotema = capturar_apotema()
area = hacer_area(perimetro, apotema)
mensaje = hacer_mensaje(area)

imprimir = imprimir_mensaje(mensaje)

