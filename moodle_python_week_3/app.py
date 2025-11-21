import servicios as serv
import archivo as csv



def dato_int(msg):
       
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
    while True:
        v_usuario = input(msg).lower
        v_bool = v_usuario
        try:    
            if v_bool != "s" or v_bool != "si" or v_bool != "n" or v_bool != "no":
                print("Debe ingresar Si o No.")
                continue

            if v_bool == "s" or v_bool == "si":
                  v_bool = True
            elif v_bool == "n" or v_bool == "si":
                  v_bool = False

            return v_bool
        
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
                serv.calcular_estadisticas(inventario)

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
                if input("> ").strip().upper() == "S":
                    inventario = nuevos
                    print("Inventario reemplazado.")
                else:
                    print("Fusionando inventarios...")
                    for p in nuevos:
                        existente = serv.buscar_producto(inventario, p["nombre"])
                        if existente:
                            # Política: sumar cantidad y actualizar al nuevo precio
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
            
    
     
