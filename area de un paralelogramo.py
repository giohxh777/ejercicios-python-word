#******area de un paralelogramo ******
#*******zona de funciones ********
def capturar_base ():
    h = int(input("digite el valor de la base: "))
    return h

def capturar_altura ():
    altura = int(input("digite el valor de la altura: "))
    return altura

def hacer_area (h, altura):
    area = (h * altura )
    return area

def hacer_mensaje(area):
    mensaje = "la area del paralelogramo es: " + str(area)
    return mensaje 

def imprimir_mensaje(mensaje):
    print (mensaje)
    
    
#***** zona codigo principal*******

h = capturar_base()
altura = capturar_altura()
area = hacer_area(h, altura)
mensaje = hacer_mensaje(area)
imprimir = imprimir_mensaje(mensaje)