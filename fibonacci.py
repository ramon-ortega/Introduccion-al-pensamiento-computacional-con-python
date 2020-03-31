print('Programa que calcula la secuencia de fibonacci')

def fibonacci(n):
    """Funcion que regresa la secuencia de fibonacci hasta n

    :param n: int >= 0
    :return: n fibonacci
    """

    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)



if __name__ == '__main__':
    n = int(input('Ingresa un numero: '))

    print(fibonacci(n))