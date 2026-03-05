ventas = []

def registrar_venta():
    producto = input("Ingrese el producto vendido: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))

    venta = {
        "producto": producto,
        "cantidad": cantidad
    }

    ventas.append(venta)
    print("Venta registrada correctamente")

def mostrar_ventas():
    if len(ventas) == 0:
        print("No hay ventas registradas")
    else:
        print("\nHistorial de ventas:")
        for compra in ventas:
            print("Producto:", compra["producto"], "| Cantidad:", compra["cantidad"])

