ciudades= [
          ["LATACUNGA", ["LUNES", 15], ["MARTES", 13],["MIERCOLES",14],["JUEVES",11],["VIERNES",12]],
          ["AMBATO",     ["LUNES",18],["MARTES",17],["MIERCOLES", 14],["JUEVES",15],["VIERNES",16]],
          ["SAQUISILI", ["LUNES",13],["MARTES",14],["MIERCOLES",12],["JUEVES",11],["VIERNES",10]], 
 ]

def promedios_temperatura(ciudades):  
    promedios = {}
    for ciudad in ciudades:
        nombre = ciudad[0]         
        datos = ciudad[1:]          
        suma = 0                  
        for dia in datos:
         suma += dia[1]          
        promedio = suma / len(datos)  
        promedios[nombre] = promedio  
    return promedios
resultado = promedios_temperatura(ciudades)

for ciudad in resultado:
    print("Temperatura promedio", ciudad, int(resultado[ciudad])) 
