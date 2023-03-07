from Lector import Lector
from Menu import Menu
from Producto import Producto
from Sucursal import Sucursal
from Empleado import Empleado
import sys

class Main:
    def main():
        """
        Función principal.
        """
        accion = 0
        while(True):
            Menu.menuAccion()
            try:
                accion = int(input("Acción: "))

                while(accion < 1 or accion > 5):
                    Menu.menuError()
                    accion = int(input("Acción: "))

            except:
                Menu.menuError()
            else:
                break

        if(accion == 5):
            sys.exit(0)

        entidad = 0

        while(True):
            Menu.menuEntidad()
            try:
                entidad = int(input("Entidad: "))

                while(entidad < 1 or entidad > 4):
                    Menu.menuError()
                    entidad = int(input("Entidad: "))
            except:
                Menu.menuError()
            else:
                break
            
        if(entidad == 4):
            sys.exit(0)

        id = ""

        if (accion != 1):
            Menu.menuID()
            id = input("ID/CURP: ")
            while (id == ""):
                Menu.datoError()
                id = input("ID/CURP: ")

        if (accion == 2):
            dato = Lector.imprime(entidad, id)
            if(dato == ""):
                print(f"El ID {id} no pudo ser encontrado.")
        else:
            if (entidad == 1):
                if (accion == 1):
                    Empleado.agrega()
                    print("Empleado agregado con éxito")
                elif (accion == 3):
                    Empleado.edita(id)
                else:
                    Empleado.elimina(id)
            elif (entidad == 2):
                if (accion == 1):
                    Producto.agrega()
                    print("Producto agregado con éxito")
                elif (accion == 3):
                    Producto.edita(id)
                else:
                    Producto.elimina(id)
            else:
                if (accion == 1):
                    Sucursal.agrega()
                    print("Sucursal agregada con éxito")
                elif (accion == 3):
                    Sucursal.edita(id)
                else:
                    Sucursal.elimina(id)
    main()        

    if __name__ == "__main__":
        main()


#TODO Opción de salir
#TODO Checar si debería repetirse el código para múltiples acciones en una ejecución