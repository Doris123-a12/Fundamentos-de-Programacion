

ciudades= [
          ["LATACUNGA", ["LUNES", 15], ["MARTES", 13],["MIERCOLES",14],["JUEVES",11],["VIERNES",12]],
          ["AMBATO",     ["LUNES",18],["MARTES",17],["MIERCOLES", 14],["JUEVES",15],["VIERNES",16]],
          ["SAQUISILI", ["LUNES",13],["MARTES",14],["MIERCOLES",12],["JUEVES",11],["VIERNES",10]], 
 ]

suma_temperatura = 0
print ("Ciudades")
for ciudad in ciudades:
    print(ciudad[0])
    for dia in ciudad [1:]:
        suma_temperatura += dia [1]

    print ("Promedio:", suma_temperatura/5)    
    suma_temperatura = 0