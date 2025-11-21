


def agregar_producto(inventario, nombre, precio, cantidad):
    """la funcion recibe una lista y datos de un producto y añade un dicionario con esos datos a la lista.

    Args:
        inventario (list): Lista de dicts con productos.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad disponible.
    """
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
        })
    print("Se agrego el producto exitosamente")


def mostrar_inventario(inventario):
    """La funcion muestra los datos en inventarios. 

    Argumento:
        inventario (list): Lista de dicts con productos.
    """
    print("---Invenatrio---\n")
    for i in inventario:
        print(f"+ nombre: {i["nombre"]} - precio: {i["precio"]} - cantidad: {"cantidad"}")
        print("---------------------------------------------------------")

def buscar_producto(inventario,nombre):
    """La funcion retorna un diccionario si se encuntra el nombre del producto en el inventario.

    Args:
        inventario (list): Lista de dicts con productos.
        nombre (str): Nombre del producto a buscar.
    """
    
    producto = next((i for i in inventario if i["nombre"] == nombre), None)
    return(producto)

def actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
    """La funcion actualiza el precio y cantidad de un producto en el inventario.

    Args:
        inventario (list): Lista de dicts con productos.
        nombre (str): Nombre del producto para actualizar.
        nuevo_precio (float): Precio  para actualizar.
        nueva_cantidad (int): Cantidad para actualizar.

    Returns:
        dict o None: Retorna el producto actualizado si existe, si no retorna None
    """

    for i in inventario:
        if i["nombre"] == nombre:
            i.update({
                "precio": nuevo_precio,
                "cantidad": nueva_cantidad
            })
            print(f"{nombre} se actualizo exitosamente")
            return i
        else:
            print(f"El producto {nombre} no esta en inventario")
            return None
        
    
def eliminar_producto(inventario, nombre):
    """Si el producto esta en inventario lo elimina 

    Args:
        inventario (list): Lista de dicts con productos.
        nombre (str): Nombre del producto a eliminar.

    Returns:
        dict: Producto eliminado.
    """
    for i in inventario:
        if i["nombre"] == nombre:
            inventario.pop(i)
            print(f"{nombre} Se elimino exitosamente")
            return i
        else:
            print(f"El producto {nombre} no esta en inventario")


def calcular_estadisticas(inventario):
    """Se realizan la metricas y retorna un diccionario con ellas

    Args:
        inventario (list): Lista de dicts con productos.

    Returns:
        dict: retorna metrica que contiene un dicionario con las metricas
    """
   
    unidades_totales = int(sum(p["cantidad"] for p in inventario))

    subtotal = lambda p: p["precio"] * p["cantidad"]

    valor_total = float(sum(subtotal(p) for p in inventario))

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])

    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    metrica = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock,

    }
    return metrica