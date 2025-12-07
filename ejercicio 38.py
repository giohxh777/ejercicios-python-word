#*********programa que pida dos numeros y muestre el mayor***********
#******** zona de funciones *************
def capturar_numeros():
    num1 = int(input("Digite el primer numero entero: "))
    num2 = int(input("Digite el segundo numero entero: "))
    return num1, num2
def determinar_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
def hacer_mensaje(mayor):
    mensaje = "El numero mayor es: " + str(mayor)
    return mensaje
def imprimir_mensaje(mensaje):

    print(mensaje)
#******** zona codigo principal ************
num1, num2 = capturar_numeros()
mayor = determinar_mayor(num1, num2)
mensaje = hacer_mensaje(mayor)
imprimir_mensaje(mensaje)
