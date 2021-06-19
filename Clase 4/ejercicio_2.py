def verificar_mayor(edad_1,edad_2,edad_3,edad_4):
    if edad_1 >= edad_2 and edad_1 >= edad_3 and edad_1 >= edad_4:
        print('Edad maxima es: ' + str(edad_1) + ',1')
    elif edad_2> edad_1 and edad_2 > edad_3 and edad_2 > edad_4:
        print('Edad maxima es: ' + str(edad_2) + ',2')
    elif edad_3 > edad_1 and edad_3 > edad_2 and edad_3 > edad_4:
        print('Edad maxima es: ' + str(edad_3) + ',3')
    else:
        print('Edad maxima es: ' + str(edad_4) + ',4')

## verificar_mayor(10,19,28,37)
verificar_mayor(15, 48, 45, 25)
verificar_mayor(15, 28, 25, 35)
verificar_mayor(15, 58, 45, 65)

edad = 58
genero = 'F'
semanas = 240

if genero == 'F':
    if edad >= 58:
        if semanas >= 250:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 250 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 58 - edad ) +' años')
elif genero == 'M':
    if edad >= 60:
        if semanas >= 255:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 255 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 60 - edad ) +' años')
