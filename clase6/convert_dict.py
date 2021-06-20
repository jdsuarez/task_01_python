tripulantes = ['p1','p2','p3','p4']

tripulantes_dict = {tripulante : '5' for tripulante in tripulantes}
print(tripulantes_dict)

tripulantes_dict = dict.fromkeys(tripulantes, 5)
print(tripulantes_dict)

tripulantes_dict = dict(zip(tripulantes, range(0,len(tripulantes))))
print(tripulantes_dict)
