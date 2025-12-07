#*********kilometros a millas*********
def kilometros_a_millas(km):
    millas = km * 0.621371
    return millas    
def hacer_mensaje(millas):
    mensaje = str(round(millas, 2)) + " millas"
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
kilometros = float(input("Digite la cantidad de kilometros a convertir a millas: "))
millas = kilometros_a_millas(kilometros)
mensaje = hacer_mensaje(millas)
imprimir_mensaje(mensaje)
