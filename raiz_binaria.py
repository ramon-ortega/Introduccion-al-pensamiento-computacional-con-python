print('Programa que calcula la raiz de un numero por medio de busqueda binaria')

numero = int(input('Ingrese un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, numero)
respuesta = (bajo + alto) / 2.0

while abs (respuesta**2 - numero) >= epsilon:
    if respuesta**2 < numero:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (bajo + alto) / 2

print(f'La raiz cuadrada de {numero} es {respuesta}')



if __name__ == '__main__':
    pass