print('Programa que al ingresar un numero te dice si tiene raiz cuadrada exacta')

numero = int(input('Ingresa un numero: '))
respuesta = 0

while respuesta ** 2 < numero:
    respuesta += 1

if respuesta**2 == numero:
    print(f'La raiz de {numero} es {respuesta}')
else:
    print(f'El numero no tiene raiz exacta')

if __name__ == '__main__':
    pass