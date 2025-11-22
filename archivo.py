import csv



def guardar_csv(inventario, ruta, header):
    """Guarda el inventario en un archivo CSV.
    
    Args:
        inventario (list): lista de productos.
        ruta (str): ruta del archivo CSV.
        header (bool): incluir encabezados.
    Returns:
        None
    """
    if not inventario:
        print("El inventario está vacío. No se guardó el archivo.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Error: No tienes permiso para escribir en esa ubicación.")
    except Exception as e:
        print(f"Error inesperado al guardar: {e}")


def cargar_csv(ruta):
    """Carga un archivo CSV como inventario.
    
    Validations:
        - Encabezado correcto
        - 3 columnas por fila
        - precio -> float no negativo
        - cantidad -> int no negativo
        - Filas inválidas se omiten y se cuentan
    Args: 
        ruta (str): ruta del archivo CSV.
    Returns:
        tuple: (lista_productos, filas_invalidas)
    """
    productos = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)

            if header != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo no tiene el encabezado correcto.")
                return None, 0

            for fila in reader:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except:
                    filas_invalidas += 1

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return None, 0
    except UnicodeDecodeError:
        print("Error: Codificación inválida del archivo.")
        return None, 0
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None, 0

    return productos, filas_invalidas