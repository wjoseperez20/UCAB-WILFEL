## Clase PizzaCliente, atributos: tamano, ingredientes.
## tamano: Tamaño de la pizza, atributo de tipo de dato TamanoPizza
## ingredientes: Ingredientes que posee la pizza, atributo de tipo lista de tipo de dato Ingrediente.
class PizzaCliente:

    def __init__(self, identificador):
        self.ingredientes = []
        self.identificador = identificador
        self.tamano = None

    def agregarIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def asignarTamano(self, tamano):
        self.tamano = tamano

    def calcularPrecio(self):
        precio = self.tamano.precio

        for ingrediente in self.ingredientes:
            precio += ingrediente.precio

        return precio
