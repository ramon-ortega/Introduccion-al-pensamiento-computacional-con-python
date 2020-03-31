print('Programa que calcula la aproximacion de la raiz cuadrada de cualquier numero')

numero = int(input('Ingresa un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while (abs(respuesta**2 - numero)) >= epsilon and respuesta < numero:
    respuesta += paso

print(f'La raiz cercana a {numero} es {respuesta}')

if __name__ == '__main__':
    pass