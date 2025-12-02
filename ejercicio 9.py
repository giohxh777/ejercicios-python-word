#*********area de un trapecio*********
#*********zona de funciones************

def definir_base_mayor():
    b1 = float(input("Digite la longitud de la base mayor: "))
    return b1

def definir_base_menor():
    b2 = float(input("Digite la longitud de la base menor: "))
    return b2

def definir_altura():
    h = float(input("Digite la altura del trapecio: "))
    return h

def calcular_area(b1, b2, h):
    area = ((b1 + b2) / 2) * h
    return area

def hacer_mensaje(area, b1, b2, h):
    b1_s = str(round(b1, 2))
    b2_s = str(round(b2, 2))
    h_s = str(round(h, 2))
    area_s = str(round(area, 2))
    mensaje = b1_s + " (base mayor) , " + b2_s + " (base menor) , altura " + h_s + " : Área: " + area_s
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)


#*******codigo principal********

b1 = definir_base_mayor()
b2 = definir_base_menor()
h = definir_altura()
area = calcular_area(b1, b2, h)
mensaje = hacer_mensaje(area, b1, b2, h)
imprimir_mensaje(mensaje)




