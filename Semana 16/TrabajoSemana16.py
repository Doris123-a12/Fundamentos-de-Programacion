# archivo: TrabajoSemana16.py
# Semana 16 - Fundamentos de Programación
# Objetivo: crear my_notes.txt, escribir 3+ líneas, leer línea por línea con readline()
# y mostrar cada línea en consola. Se cierran los archivos explícitamente con close().

ARCHIVO = "my_notes.txt"

# ---- ESCRITURA ----
salida = open(ARCHIVO, "w", encoding="utf-8")
try:
    salida.write("Registro 1: Práctica de archivos de texto con Python.\n")
    salida.write("Registro 2: Uso de write() para guardar varias líneas.\n")
    salida.write("Registro 3: Lectura posterior con readline() línea por línea.\n")
    # Puede añadir más si desea:
    salida.write("Registro 4: Cerrar archivos garantiza que se guarden los cambios.\n")
finally:
    salida.close()  # cierre obligatorio

# ---- LECTURA LÍNEA POR LÍNEA ----
entrada = open(ARCHIVO, "r", encoding="utf-8")
try:
    while True:
        linea = entrada.readline()   # devuelve '' cuando no hay más líneas
        if not linea:
            break
        print(linea.rstrip("\n"))    # mostramos sin salto extra
finally:
    entrada.close()  # cierre obligatorio

# (opcional) verificación rápida
# print("Cerrado escritura:", salida.closed, "| Cerrado lectura:", entrada.closed)
