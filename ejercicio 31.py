#************horas a minutos*************
#******** zona de funciones *************
def capturar_horas():
    horas = int(input("Digite la cantidad de horas a convertir a minutos: "))
    return horas
def convertir_a_minutos(horas):
    minutos = horas * 60
    return minutos
def hacer_mensaje(minutos):
    mensaje = str(minutos) + " minutos"
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
horas = capturar_horas()
minutos = convertir_a_minutos(horas)
mensaje = hacer_mensaje(minutos)
imprimir_mensaje(mensaje)
