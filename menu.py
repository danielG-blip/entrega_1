def mostrar_menu():
    print("Menú Principal")
    print("1. Registrar producto")
    print("2. Ver productos")
    print("3. Registrar venta")
    print("4. Ver ventas")
    print("5. Ver total del inventario")
    print("6. Salir")

def ejecutar_opcion(opcion, productos, ventas):
    if opcion == "1":
        nombre = input("Ingrese nombre del producto: ")
        precio = float(input("Ingrese precio del producto: "))
        stock = int(input("Ingrese stock inicial: "))
        productos.append({"nombre": nombre, "precio": precio, "stock": stock})
        print("Producto registrado.")

    elif opcion == "2":
        print("Lista de productos")
        for p in productos:
            print(f"{p['nombre']} - Precio: {p['precio']} - Stock: {p['stock']}")

    elif opcion == "3":
        nombre = input("Ingrese nombre del producto vendido: ")
        cantidad = int(input("Ingrese cantidad vendida: "))
        for p in productos:
            if p["nombre"] == nombre:
                if cantidad <= p["stock"]:
                    p["stock"] -= cantidad
                    ventas.append({"producto": nombre, "cantidad": cantidad, "total": cantidad * p["precio"]})
                    print("Venta registrada.")
                else:
                    print("Stock insuficiente.")
                break
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        print("Lista de ventas")
        for v in ventas:
            print(f"Producto: {v['producto']} - Cantidad: {v['cantidad']} - Total: {v['total']}")

    elif opcion == "5":
        total_inventario = sum(p["precio"] * p["stock"] for p in productos)
        print(f"Valor total del inventario: {total_inventario}")

    elif opcion == "6":
        print("Saliendo del sistema...")
        return False

    else:
        print("Opción inválida.")
    return True
