diccionario = {'calve':'valor'}
diccionario = {'nombre 1':'Juan','edad 1':23,'lenguajes':{1:'python',
                                                          2:'c++',
                                                          3:'Java',
                                                          4:'php',
                                                          5:'javascript',
                                                          6:'c#'}}
print(len(diccionario))
print(len(diccionario['lenguajes']))
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

autos = {'autos':{1:{'marca':'tesla','modelo':{1:'m1',
                                               2:'m2',
                                               3:'m3',
                                               4:'m4',
                                               5:'m5'}},
                  2:{'marca':'Toyota','modelo':{1:'m1',
                                                2:'m2',
                                                3:'m3',
                                                4:'m4'}},
                  3:{'marca':'Mazda','modelo':{1:'m1',
                                               2:'m2',
                                               3:'m3'}},
                  4:{'marca':'land rover','modelo':{1:'m1',
                                                    2:'m2'}},
                  5:{'marca':'Audi','modelo':{1:'m1'}},
                 }
        }

print(len(autos))

m1 = len(autos['autos'][1]['modelo'])
m2 = len(autos['autos'][2]['modelo'])
m3 = len(autos['autos'][3]['modelo'])
m4 = len(autos['autos'][4]['modelo'])
m5 = len(autos['autos'][5]['modelo'])
print(m1,m2,m3,m4,m5)

def verificar_mayor(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        print('1 '+ str(n1))
    elif n2 > n3 > n4 > n5:
        print('2 '+ str(n2))
    elif n3 > n4 > n5:
        print('3 '+ str(n3))
    elif n4 > n5:
        print('4 '+ str(n4))
    else:
        print('5 '+ str(n4))


# verificar_mayor(48, 48, 45, 45)
# verificar_mayor(65, 58, 45, 65)
verificar_mayor(m1,m2,m3,m4,m5)

diccionario = {'a':{'nombre1':'Marco', 'edad1':31, 'lenguajes':{
                1:'Python',
                2:'C++',
                3:'Java',
                4:'PHP',
                5:'JavaScript',
                6:'C#'}
               },'b':{'nombre1':'Juan', 'edad1':21, 
               'lenguajes':{
                1:'Python',
                2:'C++',
                3:'Java'}
               }}

for key in diccionario.keys():
    print(key)

for value in diccionario.values():
    print(value)

for key, value in diccionario.items():
    print(key)
    print(value)
