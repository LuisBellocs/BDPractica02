from Lector import Lector
from Menu import Menu
from Producto import Producto
from Sucursal import Sucursal
from Empleado import Empleado

accion = 0

while(True):
    Menu.menuAccion()
    try:
        accion = int(input("Acción: "))

        while(accion < 1 or accion > 4):
            Menu.menuError()
            accion = int(input("Acción: "))

    except:
        Menu.menuError()
    else:
        break

entidad = 0

while(True):
    Menu.menuEntidad()
    try:
        entidad = int(input("Entidad: "))
        
        while(entidad < 1 or entidad > 3):
            Menu.menuError()
            entidad = int(input("Entidad: "))
    except:
        Menu.menuError()
    else:
        break

id = 0

if (accion != 1):
    Menu.menuID()
    id = input("ID (CURP, si es empleado): ")
    print("\n")

if (accion == 2):
    Lector.lee(entidad, id)
else:
    if (entidad == 1):
        if (accion == 1):
            Empleado.agrega()
        elif (accion == 3):
            Empleado.edita(id)
        else:
            Empleado.elimina(id)
    elif (entidad == 2):
        if (accion == 1):
            Producto.agrega()
        elif (accion == 3):
            Producto.edita(id)
        else:
            Producto.elimina(id)
    else:
        if (accion == 1):
            Sucursal.agrega()
        elif (accion == 3):
            Sucursal.edita(id)
        else:
            Sucursal.elimina(id)    

#TODO Opción de salir
#TODO Checar si debería repetirse el código para múltiples acciones en una ejecución