#funcion que define que numero es mayor
a = 0
b = 0
c = 0
def que_numero_es_mayor(a, b, c):
    if a > b and a > c:
         R = a

    elif b > a and b > c:
        R = b
    elif c > a and c > b:
          R = c
    else:
         R = a, b, c
    return R
def pedir_numero(a):
    a = int(input("Digite un numero: "))
    return a
#Inicia la definicion de valor de las variables
a = pedir_numero(a)
b = pedir_numero(b)
c = pedir_numero(c)
#Se llama a la funcion

Resultado = que_numero_es_mayor(a, b, c)

print("El resultado es: {}".format(Resultado))

