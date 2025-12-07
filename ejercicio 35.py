#***********cantidad de dinero en una cuenta y calcule el 5% de interes***********
#******** zona de funciones *************
def capturar_dinero():
    dinero = float(input("Digite la cantidad de dinero en la cuenta: "))
    return dinero
def calcular_interes(dinero):
    interes = dinero * 0.05
    return interes
def hacer_mensaje(interes):
    mensaje = "El interes ganado es de: " + str(round(interes, 2)) + " euros"
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
dinero = capturar_dinero()
interes = calcular_interes(dinero)
mensaje = hacer_mensaje(interes)
imprimir_mensaje(mensaje)
