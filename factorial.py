print('Programa que calcula el factorial de un numero')

def factorial(n):
    """Funcion que regresa el factorial de n

    :param n: int > 0
    :return: n!
    """

    if n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input('Escribe un numero: '))

    print(factorial(n))