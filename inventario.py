from inventario import producto
import productos

def calcular_total_productos(lista_productos):
    total = 0

    for producto in lista_productos:
        total += producto["cantidad"]

    return total


total = calcular_total_productos(productos)

print("Total de productos en inventario:", total)