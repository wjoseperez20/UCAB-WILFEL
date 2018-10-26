from sizePizza import TamanoPizza
from IngredientePizza import Ingrediente
from PizzaCliente import PizzaCliente

## Se inicializa el arreglo vacio para listar las pizzas que ordene el cliente.
listaPizzas = []

## Se inicializan los diferentes tamaños de pizza disponibles.
grande = TamanoPizza('Grande', 580, 'g')
mediana = TamanoPizza('Mediana', 430, 'm')
personal = TamanoPizza('Personal', 280, 'p')

## Se inicializan los posibles ingredientes que llevará cada pizza.
jamon = Ingrediente('Jamón', 40, 'ja')
champinion = Ingrediente('Champiñones', 35, 'ch')
pimenton = Ingrediente('Pimentón', 30, 'pi')
dobleQueso = Ingrediente('Doble Queso', 40, 'dq')
aceituna = Ingrediente('Aceitunas', 57.5, 'ac')
pepperoni = Ingrediente('Pepperoni', 38.5, 'pp')
salchichon = Ingrediente('Salchichón', 62.5, 'sa')

## Divisor que se utiliza para la parte gráfica de la aplicación.
divisor = '******************************'


## Se inicializa la lista de tamaños que seleccionará el cliente, se ingresan los 3 tamaños definidos anteriormente.
listaTamanos = [grande, mediana, personal]

## Se inicializa la lista de ingredientes que seleccionará el cliente, se ingresan los ingredientes definidos anteriormente.
listaIngredientes = [jamon, champinion, dobleQueso, aceituna, pepperoni, salchichon]


## Función para guardar la instancia del objeto pizza dentro de la lista de pizzas definida anteriormente.
def AsignarPizza(pizza):
    listaPizzas.append(pizza)

## Función que calcula y retorna el precio total de compra, sumando el calculo de precio de cada pizza pedida por el cliente.
def CalcularPrecioTotal():
    precio = 0

    for pizza in listaPizzas:
        precio += pizza.calcularPrecio()

    return precio


## Mediante el valor que ingresa el cliente en la consola, se obtiene la instancia real del objeto tamaño.
def ObtenerTamano(identificador):
    tamanoEncontrado = None

    for size in listaTamanos:
        if identificador == size.valorSeleccion:
            tamanoEncontrado = size
            break
        
    return tamanoEncontrado

## Mediante el valor que ingresa el cliente en la consola, se obtiene la instancia real del objeto ingrediente.
def ObtenerIngrediente(identificador):
    ingredienteEncontrado = None

    for ingrediente in listaIngredientes:
        if identificador == ingrediente.valorSeleccion:
            ingredienteEncontrado = ingrediente
            break

    return ingredienteEncontrado

## Función que permite imprimir la lista de tamaños definida anteriormente.
def ImprimirTamanos():
    print('***** LISTA DE TAMAÑOS *****')
    for size in listaTamanos:
        print('=> ',size.nombre, '[', size.valorSeleccion, ']', '- Precio:', size.precio, 'Bfs')
    print('')

## Función que desplega el segmento del menú para que el cliente pueda seleccionar un tamaño.
def MenuSeleccionarTamano(pizza):
    valido = False
    while not valido:
        value = input('Seleccione un tamaño: ')
        tamano = ObtenerTamano(value)
        valido = validarValorIngresado(tamano)
        if not valido:
            print('=> Ingrese un tamaño correcto!!')
        else:
            pizza.asignarTamano(tamano)
            print('Tamaño seleccionado:', tamano.nombre, '\n')

## Función que concatena y retorna todos los ingredientes pertenecientes a una pizza en un string.
def ImprimirIngredientesSeleccionados(pizza):
    lista = ''
    for ingrediente in pizza.ingredientes:
        lista += ingrediente.nombre + ' '
    return lista

## Función que muestra los ingredientes seleccionados una vez se finaliza la selección de los mismos.
def finalizarSeleccionIngredientes(pizza):
    if len(pizza.ingredientes) < 1:
        print('Usted seleccionó una pizza', pizza.tamano.nombre, 'margarita \n')
    else:
        print('Usted seleccionó una pizza', pizza.tamano.nombre, 'con:', ImprimirIngredientesSeleccionados(pizza), '\n')

## Función que permite imprimir la lista de ingredientes definida anteriormente.
def ImprimirIngredientes():
    print('***** LISTA DE INGREDIENTES *****')
    for ingrediente in listaIngredientes:
        print('=> ',ingrediente.nombre, '[', ingrediente.valorSeleccion, ']', '- Precio:', ingrediente.precio, 'Bfs')
    print('')

## Función que desplega el segmento del menú para que el cliente pueda seleccionar los ingredientes.
def MenuSeleccionarIngredientes(pizza):
    finSeleccion = False
    while not finSeleccion:
        value = input('Seleccione un ingrediente (enter para finalizar):')

        if len(value) < 1:
            finalizarSeleccionIngredientes(pizza)
            finSeleccion = True
        else:
            ingrediente = ObtenerIngrediente(value)
            valido = validarValorIngresado(ingrediente)
            if not valido:
                print('=> Ingrese un ingrediente correcto!!')
            else:
                pizza.agregarIngrediente(ingrediente)

## Función que desplega el segmento del menú para que el cliente pueda finalizar o continuar el pedido.
def MenuContinuarPedido():
    fin = False
    print(divisor)
    valido = False
    while not valido:
        value = input('Desea continuar? [s/n]:')
        if value == 's':
            valido = True
        elif value == 'n':
            valido = True
            fin = True
        else:
            print('=> Seleccione una opción valida !!')
    print(divisor)
    return fin         

## Función que retorna un booleano dependiendo si el argumento de la función es None o no.
def validarValorIngresado(valor):
    if valor is None:
        return False
    return True




## Variable que permite detener el Loop del menú principal
fin = False

mensajeInicial = '***** PIZZERÍA DON WILFEL ***** \n'

print(mensajeInicial)

## Loop que despliega el menú principal de la aplicación
while not fin :
    pizza = PizzaCliente()
    AsignarPizza(pizza)
    print('Pizza Número:', len(listaPizzas), '\n')
    ImprimirTamanos()
    MenuSeleccionarTamano(pizza)
    ImprimirIngredientes()
    MenuSeleccionarIngredientes(pizza)
    print('Subtotal a pagar por una pizza', pizza.tamano.nombre,':',pizza.calcularPrecio(), 'Bfs \n')
    fin = MenuContinuarPedido()

print('El pedido tiene un total de', len(listaPizzas), 'pizza(s) por un valor de', CalcularPrecioTotal(),'Bfs')
print('Gracias por su compra, regrese pronto!')
