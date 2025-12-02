#*********convertir celsius a fahrenheit*********
#*********zona de funciones************

def definir_celsius():
    celsius = float(input("Digite el valor en grados Celsius: "))
    return celsius

def convertir_a_fahrenheit(celsius):
    fahrenheit = float((celsius * 9/5) + 32)
    return fahrenheit

def hacer_mensaje(celsius, fahrenheit):
    mensaje = str(celsius) + " Celsius = " + str(fahrenheit) + " Fahrenheit"
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)


#*******codigo principal********

celsius = definir_celsius()
fahrenheit = convertir_a_fahrenheit(celsius)
mensaje = hacer_mensaje(celsius, fahrenheit)
imprimir_mensaje(mensaje)


