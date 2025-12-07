#*********determinar si un numero es multiplo de otro ***********
#******** zona de funciones *************
def capturar_numeros():
    num1 = int(input("Digite el primer numero entero: "))
    num2 = int(input("Digite el segundo numero entero: "))
    return num1, num2
def es_multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
def hacer_mensaje(es_multiplo):
    if es_multiplo:
        mensaje = "El primer numero es multiplo del segundo numero."
    else:
        mensaje = "El primer numero no es multiplo del segundo numero."
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
num1, num2 = capturar_numeros()
multiplo = es_multiplo(num1, num2)
mensaje = hacer_mensaje(multiplo)
imprimir_mensaje(mensaje)
