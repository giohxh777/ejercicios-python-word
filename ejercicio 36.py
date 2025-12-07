#programa que pida dos numeros enteros y muestre el cociente de la division*********
#******** zona de funciones *************
def capturar_numeros():
    num1 = int(input("Digite el primer numero entero: "))
    num2 = int(input("Digite el segundo numero entero: "))
    return num1, num2
def calcular_cociente(num1, num2):
    cociente = num1 / num2
    return cociente
def hacer_mensaje(cociente):
    mensaje = "El cociente de la division es: " + str(cociente)
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
num1, num2 = capturar_numeros()
cociente = calcular_cociente(num1, num2)
mensaje = hacer_mensaje(cociente)
imprimir_mensaje(mensaje)
