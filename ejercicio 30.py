#******solicitar radio de un circulo y calcular la circunferencia*******
#******** zona de funciones *************
def capturar_radio():
    radio = float(input("digite el valor del radio del circulo: "))
    return radio
def calcular_circunferencia(radio):
    circunferencia = 2 * 3.1416 * radio
    return circunferencia
def hacer_mensaje(circunferencia):
    mensaje = "la circunferencia del circulo es: " + str(circunferencia)
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
radio = capturar_radio()
circunferencia = calcular_circunferencia(radio)
mensaje = hacer_mensaje(circunferencia)
imprimir_mensaje(mensaje)
