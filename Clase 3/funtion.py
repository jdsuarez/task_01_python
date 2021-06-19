def calculate_double(numero):
    print(numero*2)


calculate_double(10)


def calculate_square(numero:int):
    print(numero*numero)


paramiter = int(input('Itroduce a number: '))
calculate_square(paramiter)

def total_sum(num_1, num_2, num_3) -> float:
    return num_1 + num_2 + num_3

print(total_sum(1,2,3)) 

def promedio():
    numero_1 = int(input('Numero 1: '))
    numero_2 = int(input('Numero 2: '))
    numero_3 = int(input('Numero 3: '))
    total = total_sum(numero_1,numero_2,numero_3)
    return total/3


print(promedio())