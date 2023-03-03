string_opciones = """¿Qué acción desea realizar? 
[1] Consultar empleados
[2] Consultar sucursales 
[3] Consultar productos
[4] Salir\n"""

opcion_invalida = "Opción inválida. Por favor, ingrese un número del 1 al 4.\n"

string_eleccion = "Ingrese el número de su elección: "

print("¡Bienvenido!")

while True:
    print(string_opciones)
    opcion = input(string_eleccion )

    if opcion == "1":
        print("Ha seleccionado la opción de consultar empleados.\n")
        while True:
            print("¿Qué acción desea realizar?")
            print("[1] Imprimir información de empleados")
            print("[2] Agregar empleado")
            print("[3] Eliminar empleado")
            print("[4] Regresar")

            sub = input(string_eleccion)
            print("")

            if sub == "1": print("hola")
            elif sub == "2": print("hola")
            elif sub == "3": print("hola")
            elif sub == "4":
                break
            else:
                print(opcion_invalida)

    elif opcion == "2":
        print("Ha seleccionado la opción de consultar sucursales.\n")
        while True:
            print("¿Qué acción desea realizar?")
            print("[1] Imprimir información de sucursales")
            print("[2] Agregar sucursal")
            print("[3] Eliminar sucursal")
            print("[4] Regresar")
            
            sub = input(string_eleccion)
            print("")

            if sub == "1": print("hola")
            elif sub == "2": print("hola")
            elif sub == "3": print("hola")
            elif sub == "4":
                break
            else:
                print(opcion_invalida)
    elif opcion == "3":
        print("Ha seleccionado la opción de consultar productos.\n")
        while True:
            print(string_opciones)
            sub = input(string_eleccion)
            print("")

            if sub == "1": print("hola")
            elif sub == "2": print("hola")
            elif sub == "3": print("hola")
            elif sub == "4":
                break
            else:
                print(opcion_invalida)

    elif opcion == "4":
        print("¡Hasta luego!\n")
        break
    else:
        print(opcion_invalida)