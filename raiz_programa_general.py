print('Programa donde puedes calcular la raiz cuadrada de un numero eligiendo distintos metodos')
print('Los metodos es escontar la raiz cuadrada, raiz cuadrada por aproximacion y raiz cuadrada por metodo binario')
print('A continuacion seleccione el metodo:')

print('''         raiz [c]uadrada
         raiz [a]proximada
         raiz [b]inaria''')

seleccion = str(input('Ingresa la letra del metodo [*]: '))

def cuadrada(respuesta, numero):
    while respuesta ** 2 < numero:
        respuesta += 1

    if respuesta ** 2 == numero:
        print(f'La raiz de {numero} es {respuesta}')
    else:
        print(f'El numero no tiene raiz exacta')

def aproximacion(respuesta, epsilon, paso, numero):
    while (abs(respuesta ** 2 - numero)) >= epsilon and respuesta < numero:
        respuesta += paso

    print(f'La raiz cercana a {numero} es {respuesta}')

def binario(respuesta, numero, epsilon, alto, bajo):
    while abs(respuesta ** 2 - numero) >= epsilon:
        if respuesta ** 2 < numero:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (bajo + alto) / 2

    print(f'La raiz cuadrada de {numero} es {respuesta}')


if __name__ == '__main__':
    if seleccion == 'c':
        numero = int(input('Ingresa un numero: '))
        respuesta = 0
        cuadrada(respuesta, numero)
    elif seleccion == 'a':
        numero = int(input('Ingresa un numero: '))
        epsilon = 0.01
        paso = epsilon ** 2
        respuesta = 0.0
        aproximacion(respuesta, epsilon, paso, numero)
    elif seleccion == 'b':
        numero = int(input('Ingresa un numero: '))
        epsilon = 0.01
        bajo = 0.0
        alto = max(1.0, numero)
        respuesta = (bajo + alto) / 2.0
        binario(respuesta, numero, epsilon, alto, bajo)

    else:
        print('la opcion que usted selecciono no existe')


