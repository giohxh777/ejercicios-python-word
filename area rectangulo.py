#********Area de un rectangulo***********
#********Zona funciones*****************

def definir_longitud ():
    longitud = int(input("digite el valor de la base"))
    return longitud

def definir_ancho () :
    ancho = int(input("Digite el valor de la base"))
    return ancho

def hacer_area (longitud, ancho):
    area = (longitud * ancho)
    return area

def mostrar_mensaje(area):
    mensaje = "la area del rectangulo es " +str(area)
    
def imprimir_mensaje(mensaje):
        print(mensaje)
        
#***********codigo principal***************
longitud = definir_longitud ()
ancho = definir_ancho()
area = hacer_area(longitud, ancho)
mensaje = mostrar_mensaje(area)
imprimir = imprimir_mensaje (mensaje)
    