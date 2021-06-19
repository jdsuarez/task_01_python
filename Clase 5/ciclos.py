numeros = [54,58+5,45,12,57,84,64,25]

for i in numeros:
    if i%2==0:
        print(i)
    else:
        print('-')


##________________________________________________________
devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
        {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
        {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
        {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
        {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
        {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
        {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
        {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
        {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}]

print(devs[1])
s = 0
indice = 0
for i in devs:
    if i['salario'] > s:
        s = i['salario']
        indice = i

print(s)
print(indice)

actual_dev = {'salario':0}
for dev in devs:
    if dev['salario'] >= actual_dev['salario']:        
        actual_dev = dev
print(actual_dev['cc'], actual_dev['nombre'])

print('___________________ciclo while_______________________________')
i = 0
while i < len(numeros):
    # print(numeros[i])
    if numeros[i]%2==0 and numeros[i]<60:
        print(numeros[i])
    else:
        print('null')
   
    i += 1

print(devs[0]['years'])
i = 0
y_xp = 100
index = 0
while i < len(devs):
    if devs[i]['years'] < y_xp:
        y_xp = devs[i]['years']
        i = index

    i += 1

print(y_xp)
print(devs[index])