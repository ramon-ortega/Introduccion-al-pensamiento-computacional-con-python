print('Programa que pide el nombre de dos personas junto con su edad y regresa el nombre de la persona que es mayor que la otra')

nombre_1 = str(input('Ingresa el nombre de la persona numero 1: '))
edad_1 = int(input('Ingresa la edad de la persona 1: ' ))
nombre_2 = str(input('Ingresa el nombre de la persona numero 2: '))
edad_2 = int(input('Ingresa la edad de la persona 2: '))

if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}')
elif edad_1 < edad_2:
    print(f'{nombre_2} es mayor que {nombre_1}')
else:
    print(f'{nombre_1} y {nombre_2} son de la misma edad')

if __name__ == '__main__':
    pass