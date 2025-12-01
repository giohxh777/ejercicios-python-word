#*****km a millas*****
#*****zona funcional*****

def capturar_km():
    km = int(input("digite el valor de los kilometros que desea convertir: ")) 
    return km

def hacer_convercion(km):
    conversion= (km*0.621)
    return conversion

def hacer_mesaje(km, conversion ):
    mensaje = str(km) + " km convertido a millas es: " + str(conversion)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****
def main():
    km = capturar_km()
    conversion = hacer_convercion(km)
    mensaje = hacer_mesaje(km, conversion)
    imprimir_mensaje(mensaje)
if __name__ == '__main__':
    main()