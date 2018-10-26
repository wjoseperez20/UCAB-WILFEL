## Clase TamanoPizza, atributos: Nombre, Precio y valor de selección
## Nombre: Nombre del ingrediente.
## Precio: Precio del ingrediente.
## ValorSeleccion: String que permite identificar el tamaño ingresado en consola por el cliente.
class TamanoPizza:
    def __init__(self, nombre, precio, valorSeleccion):
        self.nombre = nombre
        self.precio = precio
        self.valorSeleccion = valorSeleccion
