class Menu:
    @staticmethod
    def menuAccion():
        """
        Imprime el menú de acción.
        """
        print("Elija una acción:")
        print("1) Agregar")
        print("2) Consultar")
        print("3) Editar")
        print("4) Eliminar")
        print("5) Salir")

    @staticmethod
    def menuEntidad():
        """
        Imprime de entidad.
        """
        print("Elija una entidad:")
        print("1) Empleados")
        print("2) Productos")
        print("3) Sucursales")
        print("4) Salir")

    @staticmethod
    def menuID():
        """
        Imprime el mensaje que solicita el ID.
        """
        print("Escriba el ID (CURP, si es empleado): ")

    @staticmethod
    def menuError():
        """
        Imprime el mensaje de error cuando seleccionan una opción inválida.
        """
        print("Esa no es una opción válida. Elija de nuevo.")
    
    @staticmethod
    def datoError():
        """
        Imprime el mensaje de error cuando un dato es inválido.
        """
        print("Dato no válido, escríbalo de nuevo.")