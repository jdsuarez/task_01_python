nombre = '  juan suarez  '
print(nombre)
nombre = nombre.strip()
print(nombre)
nombre = nombre.capitalize()
print(nombre)
print(nombre.count('a'))

## indices
palabra = 'un texto de muchas palabras'
print(palabra[0:5]) ## indices de o a 5
print(palabra[-5:]) ## de atras hacia adelante hasta el indice -5
print(palabra[::1]) ## palabra entera en paso de 1
print(palabra[::2]) ## todos los indices en paso de 2 en 2
print(palabra[::-1]) ## todos los indices palabra invertida