n1 = 51743
n2 = int(str(n1)[::-1])
print(n2)
n3 = str(n1)
print(str(n1)[2:])

n = (5-3)*5-7+1
usuario = 51743
print(str(usuario)[2:])
captcha = int(input('Por favor ingrese el valor de la suma: ' + str((usuario)[2:]) + ' + ' + str(n) + ' ='))

if captcha == 747:
    print('Sesión iniciada')
else:
    print('Error')