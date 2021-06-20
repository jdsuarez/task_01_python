#lista = [5,4,6,8]

#matriz = [lista,lista,lista]

#print(matriz)

#for i in matriz:
#    print(max(i))
#    print(min(i))
#    print(sum(i)/len(i))

# print(matriz[0])
# print(matriz[0][0])
# print(matriz[1][0])
# print(matriz[-1][-1])
# matriz[-1][-1] = 5
# print(matriz[-1][-1])
# print(matriz)

matriz = [[5, 7, 6, 9], [3, 4, 2, 8], [7, 9, 6, 1]]

print(len(matriz))
print(len(matriz[0]))

print('--------------------------')
print(matriz)
print('--------------------------')
i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[0]):
        if matriz[i][j]%2 != 0:
            matriz[i][j] = matriz[i][j]*2
        else:
            matriz[i][j] = matriz[i][j]/2
        j = j + 1 
    i = i + 1
print('--------------------------')

print(matriz)
print('usando ciclo for')

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] <= 4:
            matriz[i][j] = matriz[i][j]*2
        else:
            matriz[i][j] = matriz[i][j]/2

print(matriz)





