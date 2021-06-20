palabra = 'una palabra'
print(palabra)

lista = list(palabra)

diccionario = {'nombre':'lina','apellidos':'silva'}
lista = list(diccionario.keys())
print(lista)
lista = list(diccionario.values())
print(lista)
lista = list(diccionario.items())
print(lista)

tupla = tuple(diccionario.values())
print(tupla)

lista = list(palabra)
print(lista)

palabra = ''.join(lista)
print(palabra)
