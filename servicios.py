


def agregar_producto(inventario, nombre, precio, cantidad):
    """Recibe una lista(inventario) y datos de un producto y añade un dicionario con esos datos a la lista(inventario) 
    Inprime un mensaje de salidad.

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
    """Muestra los datos en inventarios mediante un bucle y los inprime o muestra
    si no hay datos en el inventaro indica con un mensaje que esta vacio. 

    Argumento:
        inventario (list): Lista de dicts con productos.
    """
    if inventario: 
        print("--Invenatrio:\n")
        for i in inventario:
            print(f"+ nombre: {i["nombre"]} - precio: {i["precio"]} - cantidad: {i["cantidad"]}")
            print("---------------------------------------------------------")
    else:
        print("Inventario Vacio")
        return 

def buscar_producto(inventario,nombre):
    """Busca el nombre de un producto en inventario y retorna el producto encontrado 
    si no esta retona None.

    Args:
        inventario (list): Lista de dicts con productos.
        nombre (str): Nombre del producto a buscar.
    """
    
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None
 
def actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
    """Actualiza el precio y cantidad de un producto en el inventario mediante un nombre e imprime un mensaje indicando si esta o no esta.
    retorna el producto

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
                "nombre": nombre,
                "precio": nuevo_precio,
                "cantidad": nueva_cantidad
            })
            print(f"{nombre} se actualizo exitosamente")
            return i
        else:
            print(f"El producto {nombre} no esta en inventario")
            return None
        
    
def eliminar_producto(inventario, nombre):
    """Elimina un prpducto de inventario mediante un nombre imprime un mensaje indicando si
    elimino el producto si o no y retorna el producto eliminado  

    Args:
        inventario (list): Lista de dicts con productos.
        nombre (str): Nombre del producto a eliminar.

    Returns:
        dict o None: Producto eliminado.
    """
    for i in inventario:
        if i["nombre"] == nombre:
            inventario.remove(i)
            print(f"{nombre} Se elimino exitosamente")
            return i
        else:
            print(f"El producto {nombre} no esta en inventario")
            return 

def calcular_estadisticas(inventario):
    """Realizan las estadisticas de inventario y retorna un diccionario con ellas

    Args:
        inventario (list): Lista de dicts con productos.

    Returns:
        dict: retorna metrica que contiene un dicionario con las metricas
    """
    if inventario:

        unidades_totales = int(sum(p["cantidad"] for p in inventario))

        subtotal = lambda p: p["precio"] * p["cantidad"]

        valor_total = float(sum(subtotal(p) for p in inventario))

        producto_mas_caro = max(inventario, key=lambda p: p["precio"])

        producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

        metrica = ({
            "unidades_totales": unidades_totales,
            "valor_total": valor_total,
            "producto_mas_caro": f"-{producto_mas_caro["nombre"]} --> Precio: {producto_mas_caro["precio"]}",
            "producto_mayor_stock": f"-{producto_mayor_stock["nombre"]} --> Cantidad: {producto_mayor_stock["cantidad"]}",

        })
        return metrica
    else:
        print("Inventario vacio")
        return