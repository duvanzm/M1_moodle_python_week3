import servicios as serv
import archivo as csv



def dato_int(msg):
    """Validad que el input se tipo int y positivo

    Args:
        msg (str): str del input

    Returns:
        v_int: El valor int validado
    """
       
    while True:
        try:
            v_int = int(input(msg))
            if v_int < 0:
                print("Debe ser un valor positivo")
                continue
            return v_int
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")         
       

def dato_float(msg):
    """Validad que el input se tipo float y positivo

    Args:
        msg (str): str del input
    Returns:
        v_float: El valor float validado
    """

    while True:
        try:
            v_float = float(input(msg))
            if v_float < 0:
                print("Debe ser un número positivo.")
                continue
            return v_float
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")              

def dato_bool(msg):
    """Validad que el dato ingresado se convierta en True y False

    Args:
        msg (str): str del input

    Returns:
        v_bool: El valor booleano True o False
    """
    while True:
        v_usuario = input(msg).strip().lower()
        v_bool = v_usuario
        try:    
            if v_usuario in ("s", "si"):
                return True

            elif v_usuario in ("n", "no"):
                return False

            else:
                print("Debe ingresar 'Si' o 'No'. Intenta de nuevo.")
                
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")              

       
def menu ():
    inventario = list()
    while True:
        print("---Menú principal---")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        print("----------------------\n")

        try:
            opcion = int(input("Elige opción (1-9): "))
        except ValueError:
            print("Opción inválida.")
            continue

        if opcion == 1:
                print("---Agregando Producto---")
                nombre = input("Ingrese el nombre: ").lower()
                precio = dato_float("Ingrese precio: ")
                cantidad = dato_int("Ingrese cantidad en stock: ")
                serv.agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
                print("---Mostrando Inventario---")
                serv.mostrar_inventario(inventario)

        elif opcion == 3:
                print("---Buscando Producto---")
                nombre = input("Ingrese nombre: ").lower()
                producto = serv.buscar_producto(inventario, nombre)
                print(f" Producto:\n {producto}")
                
                

        elif opcion == 4:
                print("---Actualizando Producto---")
                nombre = input("Ingrese nombre: ").lower()
                nuevo_precio = dato_float("Igrese el nuevo precio: ")
                nueva_cantidad = dato_int("ingrese la nueva cantidad: ")
                serv.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                      
        elif opcion == 5:
                print("---Eliminando Producto---")
                nombre = input("Ingrese nombre: ").lower()
                serv.eliminar_producto(inventario, nombre)

        elif opcion == 6:
                print("---Estadísticas del Inventario---")
                datos = serv.calcular_estadisticas(inventario)
                print("\n".join(f"{k}: {v}" for k, v in datos.items()))
                     
        elif opcion == 7:
                print("---Guardando CSV---")
                ruta = input("Nombre de la ruta: ")
                header = dato_bool("Quiere incluir encabezado (s/n): ")
                csv.guardar_csv(inventario, ruta, header)

        elif opcion == 8:
                print("---Cargar CSV---")
                ruta = input("Ruta del CSV a cargar: ")
                nuevos, invalidas = csv.cargar_csv(ruta)

                if nuevos is None:
                    continue

                print(f"{len(nuevos)} productos cargados. {invalidas} filas inválidas omitidas.")

                print("¿Sobrescribir inventario actual? (S/N)")
                if input(">").strip().upper() == "S":
                    inventario = nuevos
                    print("Inventario reemplazado.")
                else:
                    print("Fusionando inventarios...")
                    for p in nuevos:
                        existente = serv.buscar_producto(inventario, p["nombre"])
                        if existente:
                   
                            existente["cantidad"] += p["cantidad"]
                            existente["precio"] = p["precio"]
                        else:
                            inventario.append(p)
                    print("Fusión completada.")

        
        elif opcion == 9:
                print("---Saliendo---\n Bye ")
                break

        else:
            print("Opción fuera de rango.")

menu()
            
    
     
