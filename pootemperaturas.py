# Clase base que representa la información diaria del clima
class ClimaDiario:
    def __init__(self, ciudad):
        self._ciudad = ciudad            # Atributo encapsulado
        self._temperaturas = []          # Lista de temperaturas diarias

    # Método para ingresar una temperatura diaria
    def agregar_temperatura(self, temperatura):
        self._temperaturas.append(temperatura)

    # Método para obtener las temperaturas
    def obtener_temperaturas(self):
        return self._temperaturas


# Clase hija que hereda de ClimaDiario
class ClimaSemanal(ClimaDiario):

    # Polimorfismo: método que calcula el promedio semanal
    def calcular_promedio_semanal(self):
        if len(self._temperaturas) == 0:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)


# Diccionario de ciudades y temperaturas (datos de entrada)
ciudades_temperaturas = {
    "Nueva York": [22, 25, 26, 24, 23],
    "Los Ángeles": [28, 30, 29, 31, 27],
    "Chicago": [21, 20, 22, 18, 19],
    "Miami": [32, 33, 34, 30, 32],
    "Dallas": [26, 28, 27, 29, 25]
}

# Lista para almacenar los objetos de clima
climas = []

# Creamos objetos y agregamos temperaturas
for ciudad, temperaturas in ciudades_temperaturas.items():
    clima = ClimaSemanal(ciudad)
    for temp in temperaturas:
        clima.agregar_temperatura(temp)
    climas.append(clima)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for clima in climas:
    promedio = clima.calcular_promedio_semanal()
    print(f"{clima._ciudad}: {promedio:.2f}°C")
