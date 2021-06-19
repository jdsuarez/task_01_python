## datos base
# velocidad promedio 30 kM/h
# distancia total 90 km
# tiempo base de recorrido = distancia total / velocidad promedio = 3h
# tiempo base en minutos = 3*60 = 180 min
# tiempo de subida por pasagero = 2 min
# tiempo de bajada por pasagero = 1 min
def tiempo_total(num_subidas,num_bajadas) -> int:
    total_pa = num_subidas*2 + num_bajadas*1
    return total_pa + 180

print('tiempo total del recorido: '+ str(tiempo_total(int(input('Ingrese el numero de pasajeros que subieron: ')),int(input('Ingrese el numero de pasajeros que bajaron: ')))) + ' min ')
