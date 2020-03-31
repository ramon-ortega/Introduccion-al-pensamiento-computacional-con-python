def division_de_lista_entre_numero(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return print('No existe la division entre 0')

if __name__ == '__main__':
    lista = list(range(10))
    divisor = 2

    print(division_de_lista_entre_numero(lista, divisor))