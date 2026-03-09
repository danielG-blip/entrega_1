from menu import mostrar_menu, ejecutar_opcion

def main():
    productos = []
    ventas = []
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        continuar = ejecutar_opcion(opcion, productos, ventas)

if __name__ == "__main__":
    main()
