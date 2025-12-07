#********solicitar dos numeros y calcule el promedio de ambos******
#******** zona de funciones *************
def capturar_numeros():
    num1 = float(input("Digite el primer numero: "))
    num2 = float(input("Digite el segundo numero: "))
    return num1, num2
def calcular_promedio(num1, num2):
    promedio = (num1 + num2) / 2
    return promedio
def hacer_mensaje(promedio):
    mensaje = "El promedio de los dos numeros es: " + str(round(promedio, 2))
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
#******** zona codigo principal ************
num1, num2 = capturar_numeros()
promedio = calcular_promedio(num1, num2)
mensaje = hacer_mensaje(promedio)
imprimir_mensaje(mensaje)
