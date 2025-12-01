#*******Area del triangulo******
#*******zona de funciones*******

def capturar_base ():
    base= int(input("Digite la base "))
    return base

def capturar_altura ():
    altura = int(input("Digite la altura"))
    return altura
    
def formar_area(base, altura):
    area= (base*altura /2)
    return area
def mostrar_mensaje(area):
    mensaje = "El area del triangulo es" + str (area )
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#********Zona de funciones***********

dato_base = capturar_base()
dato_altura = capturar_altura()
hacer_area = formar_area (dato_base, dato_altura)
mensaje = mostrar_mensaje (hacer_area)
imprimir = imprimir_mensaje(mensaje)


    
