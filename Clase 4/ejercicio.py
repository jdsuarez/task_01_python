

edad = int(input('Introduzca su edad: '))

if edad <= 14 and edad >= 10:
    print('Categoria infantil')
elif edad <= 17 and edad >= 15:
    print('Categoria juvenil')
elif edad <= 20 and edad >= 18:
    print('Categoria Sub-20')
elif edad > 20:
    print('Categoria profesional')
else:
    print('edad no valida')

