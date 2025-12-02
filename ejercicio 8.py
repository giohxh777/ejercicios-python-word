#*********convertir dolares a euros*********
#*********zona de funciones************

def definir_dolares():
    dolares = float(input("Digite la cantidad en dólares (USD): "))
    return dolares

def definir_tasa():
    tasa = float(input("Digite la tasa de cambio (1 USD = X EUR): "))
    return tasa

def convertir_a_euros(dolares, tasa):
    euros = dolares * tasa
    return euros

def hacer_mensaje(dolares, tasa, euros):
    dolares_s = str(round(dolares, 2))
    tasa_s = str(round(tasa, 4))
    euros_s = str(round(euros, 2))
    mensaje = dolares_s + " USD = " + euros_s + " EUR (tasa: " + tasa_s + ")"
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)


#*******codigo principal********

dolares = definir_dolares()
tasa = definir_tasa()
euros = convertir_a_euros(dolares, tasa)
mensaje = hacer_mensaje(dolares, tasa, euros)
imprimir_mensaje(mensaje)



