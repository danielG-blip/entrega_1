producto = [
    {"nombre": "Camisa", "cantidad": 10},
    {"nombre": "Zapatos", "cantidad": 5},
    {"nombre": "Gorras", "cantidad": 8},
]

def calcular_total_productos(lista_productos):
    total: 0

    for producto in lista_productos:
        total += producto["Cantidad"]

        return total
    
    total = calcular_total_productos(producto)
print("Total de productos en inventario:", total)