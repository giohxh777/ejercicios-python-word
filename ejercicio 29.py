#**********determinar si un numero es par o impar con el operador modulo**********
#******** zona de funciones *************
def capturar_numero():
    numero = int(input("digite un numero entero: "))
    return numero
def determinar_par_impar(numero):
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado
def hacer_mensaje(resultado):
    mensaje = "el numero es: " + resultado
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
numero = capturar_numero()
resultado = determinar_par_impar(numero)
mensaje = hacer_mensaje(resultado)
imprimir_mensaje(mensaje)