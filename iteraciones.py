print('Iteraciones con While')

contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 3:
            break


    contador_interno = 0
    contador_externo += 1

if __name__ == '__main__':
    pass