class Menu:
    @staticmethod
    def menuAccion():
        print("Elija una acción:")
        print("1) Agregar")
        print("2) Consultar")
        print("3) Editar")
        print("4) Eliminar")
        print("5) Salir")

    @staticmethod
    def menuEntidad():
        print("Elija una entidad:")
        print("1) Empleados")
        print("2) Productos")
        print("3) Sucursales")
        print("4) Salir")

    @staticmethod
    def menuID():
        print("Escriba el ID (CURP, si es empleado): ")

    @staticmethod
    def menuError():
        print("Esa no es una opción válida. Elija de nuevo.")
    
    @staticmethod
    def datoError():
        print("Dato no válido, escríbalo de nuevo.")