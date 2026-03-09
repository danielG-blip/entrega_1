Sistema de Inventario en Python
Este proyecto es un sistema básico de inventario y ventas desarrollado en Python.
Permite registrar productos, ver el listado de productos, registrar ventas, consultar las ventas realizadas y calcular el valor total del inventario.

Estructura del proyecto
ENTREGA_1/
│
├── venv/                entorno virtual
├── pycache/          archivos generados automáticamente por Python
│
├── main.py               punto de entrada del programa
├── menu.py               funciones para mostrar y ejecutar el menú
├── productos.py          clase Producto y validaciones
├── inventario.py         lógica de inventario y ventas
│
└── Readme.md             documentación del proyecto

Requisitos
Python 3.10 o superior

Entorno virtual (venv) recomendado

Instalación
Clonar o descargar el proyecto.

Crear un entorno virtual:
python -m venv venv

Activar el entorno virtual:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Instalar dependencias (si las hubiera):
pip install -r requirements.txt

Uso
Ejecuta el archivo principal:
python main.py

El programa mostrará un menú con las siguientes opciones:

Registrar producto

Ver productos

Registrar venta

Ver ventas

Ver total del inventario

Salir

Notas
Los datos se mantienen en memoria mientras el programa está en ejecución.

Al cerrar el programa, los productos y ventas registrados se pierden (se puede extender para guardar en archivo o base de datos).