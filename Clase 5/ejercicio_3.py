students = {'a': {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]}, 'j': {'name':'Jenny','notas':[4,3.7,4,4,4.2]},\
        'c': {'name':'Ana','notas':[4.1,4.7,4.1,4.9,4.2]}, 'y': {'name':'Pedro','notas':[4,3.7,4,4,4.2]},\
            'x': {'name':'Pablo','notas':[4,3.3,3.4,3.2,3.2]}, 'l': {'name':'Carlos','notas':[3.4,3.8,4.2,4,4.1]},\
                'v': {'name':'Maria','notas':[4.8,4.7,4.6,4.9,4.8]}, 'r': {'name':'Luisa','notas':[4.8,4.7,4.5,4.5,4.9]},\
                    'b': {'name':'Mario','notas':[2.4,3.2,3.1,3.4,4.2]}, 'g': {'name':'Fabio','notas':[2.4,3.2,3.1,3.4,4.2]}}

## print(students.items())

## print(students['notas'])

# for key in students.keys():
#    print(key)

#print(students['a']['notas'])

def avg (n):
    avg = sum(n)/len(n)
    return avg

## Promedio mas alto 

av_max = 0
for key in students.keys():
    av1 = avg(students[key]['notas'])
    if av1 > av_max:
        av_max = av1
print('El promedio maximo ha sido: ' + str(av_max))

## promedio minimo

av_min = 99
for key in students.keys():
    av1 = avg(students[key]['notas'])
    if av1 < av_min:
        av_min = av1

print('El promedio minimo ha sido ' + str(av_min))

n_max = 0
n_min = 99

# nota minima

for key in students.keys():
    n_ma = min(students[key]['notas'])
    if n_ma < n_min:
        n_min = n_ma

print('La nota minima optenida ' + str(n_min))

#nota maxima

for key in students.keys():
    n_m = max(students[key]['notas'])
    if n_m > n_max:
        n_max = n_m

print('La nota máxima optenida ' + str(n_max))

matriz_1 = {}

# for values in students.values():
#    matriz_1[values] = students[values]['notas']
# print(students.items())
# print(len(matriz_1))

#for n in matriz_1:
#    print(n)

for key, value in students.items():
    print(value)
    print(key)
    matriz_1[key] = value['notas']
    

# print(matriz_1)

srp = []
nrp = []

for n in matriz_1:
    if n not in nrp:
        nrp.append(n)
    else:
        if n not in srp:
            srp.append(n)

print(srp)
print(nrp)


# por cada elemento de un iterable se guarda el elemento si cumple una condicion

nottt = [4, 3.3, 3.4, 3.2, 3.2]

nottt_c = [nota for nota in nottt if nota > 3.5]
# print(nottt_c)

