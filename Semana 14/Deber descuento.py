def calcular_descuento(cantidad_total, descuento = 15):
    valor = (cantidad_total * descuento)/100
    return valor, cantidad_total - valor

while True:
    total = float(input("Cantidad total de la compra"))
    descuento = input("Porcentaje descuento")


    if descuento == 0 or descuento == "": 
       respuesta = (calcular_descuento(total)) 
    print(f"Valor de la comprar Total: {total}")
    print(f"Total descuento: {respuesta}")
    print(f"Total valor final: {respuesta[1]}") 
else:
    respuesta = (calcular_descuento(total, int(descuento)))
    print(f"Valor de la comprar Total: {total}")
    print(f"Total descuento: {respuesta}")
    print(f"Total valor final: {respuesta[1]}") 




    