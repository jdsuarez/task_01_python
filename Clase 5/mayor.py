numeros1 = [59, 58+5, 45-5, 12*2]
numeros2 = [54, 58+5, 45, 12+24]
numeros3 = [54+2, 58+5, 45, 12]
numeros4 = [4, 58+5, 45*2, 12]

p = [sum(numeros1)/len(numeros1), sum(numeros2)/len(numeros2), sum(numeros3)/len(numeros3), sum(numeros4)/len(numeros4)]
print(p)

def verificar_mayor(n1, n2, n3, n4):
    if n1 > n2 and n1 > n3 and n1 > n4:
        print('1 '+ str(n1))
    elif n2 > n3 > n4:
        print('2 '+ str(n2))
    elif n3 > n4:
        print('3 '+ str(n3))
    else:
        print('4 '+ str(n4))

print(verificar_mayor(p[0],p[1],p[2],p[3]))

print(max(p))