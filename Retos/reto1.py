print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
# n1 = int(str(usuario)[2:]) # ultimos 3 digitos del usuario // captcha
usuario = input('Por favor ingrese su usuario: ')
contraseña = []
# cod usuario 51743 reverso 34715
if usuario != '51743' or len(usuario) == 0:
    print('Error')
    usuario = []
else:
    contraseña = input('Por favor ingrese su contraseña: ')
    if contraseña != '34715' or len(contraseña) == 0:
        print('Error')
        contraseña = []
    else:
        n = (5-3)*5-7+1
        captcha = input('Por favor ingrese el valor de la suma: ' + usuario[2:] + ' + ' + str(n) + ' = ')
        if captcha != '747' or len(captcha) == 0:
            print('Error')
        else:
            print('Sesión iniciada')
        






