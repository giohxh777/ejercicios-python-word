#******area de un paralelogramo ******
#*******zona de funciones ********
def capturar_base ():
    base = int(input("digite el valor de la base: "))
    return base

def capturar_altura ():
    altura = int(input("digite el valor de la altura: "))
    return altura

def hacer_area (base, altura):
    area = (base * altura )
    return area

def hacer_mensaje(area):
    mensaje = "la area del paralelogramo es: " + str(area)
    return mensaje 

def imprimir_mensaje(mensaje):
    print (mensaje)
    
    
#***** zona codigo principal*******

base = capturar_base()
altura = capturar_altura()
area = hacer_area(base, altura)
mensaje = hacer_mensaje(area)

imprimir = imprimir_mensaje(mensaje)
