import os
import time

opcion = True
## CONVIERTE NUMEROS A ENTERO O DECIMAL
def convertir_numeros():
    a = input("Ingrese nota: ")
    if "." in a:
        a = float(a)
    else:
        a = int(a)
    return a
## MUESTRA LOS PRIMEROS 20 NUMEROS PARES
def contar_20_primeros_pares(numero):
    numero = 0
    lista_de_pares = []
    for n in range(0, 20):
        numero += 2
        lista_de_pares.append(numero)
    print(lista_de_pares)
    print(len(lista_de_pares))
## PROMEDIA 3 NOTAS Y SI ES IGUAL O MAYOR A 4 APRUEBAS
def promedio_de_3_notas():
    n1 = convertir_numeros()
    n2 = convertir_numeros()
    n3 = convertir_numeros()
    print("Calculando.....")
    time.sleep(2)
    total = n1 + n2 + n3
    promedio = total/3
    print("el promedio es: {} por lo cual".format(promedio))
    if promedio >= 4:
        print("Su promedio es suficiente para aprobar")
    else:
        print("Su promedio es insuficiente, tendra que rendir EXAMEN")


def saludo():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Ingresa tu edad: "))

    Saludo_v = ("Hola me llamo {} {} y tengo {} años".format(nombre,apellido,edad))
    return Saludo_v

while opcion != False:
    seleccion = int(input("1.-20 primeros pares, 2.-promedio de 3 notas, 3.- Saludo\n"
                      "Elije una opcion: "))
    if seleccion == 1:
        contar_20_primeros_pares(0)
    elif seleccion == 2:
        promedio_de_3_notas()
    elif seleccion == 3:
        print(saludo())
    opcion_repetir = input("Quieres usar otro codigo? S/N: ")
    if opcion_repetir.lower() == "s":
        print("Reiniciando...")
        time.sleep(2)
        os.system("cls")
    elif opcion_repetir.lower() == "n":
        print("Saliendo")
        time.sleep(2)
        opcion = False
    else:
        print("La opcion no es valida, asi que me ire")
        print("Saliendo.....")
        time.sleep(2)
        exit()