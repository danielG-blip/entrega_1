inventario = []

def registrarNuevoProducto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad en inventario: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(f"¡{nombre} registrado con éxito!")

def mostrarProductos():
    if not inventario:
        print("El inventario está vacío actualmente")
        return

    print("Inventario Actual")

    for i, prod in enumerate(inventario, start=1):
        print(f"{i}. Producto: {prod['nombre']} | Precio: ${prod['precio']} | Stock: {prod['cantidad']} unidades")


inventario.append({"nombre": "Gorra", "precio": 25000, "cantidad": 20})
inventario.append({"nombre": "Jean", "precio": 45000, "cantidad": 30})
inventario.append({"nombre": "Camisa", "precio": 30000, "cantidad": 15})
mostrarProductos()