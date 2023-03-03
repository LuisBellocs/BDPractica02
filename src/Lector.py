import csv

class Lector:
    @staticmethod
    def lee(entidad, id):

        if (entidad == 1):
            with open('empleados.csv') as empleados:
                reader = csv.reader(empleados)
                for empleado in reader:
                    if (empleado[0] == id):
                        print(empleado)
        elif (entidad == 2):
            with open('productos.csv') as productos:
                reader = csv.reader(productos)
                for producto in reader:
                    if (producto[0] == id):
                        print(producto)
        else:
            with open('sucursales.csv') as sucursales:
                reader = csv.reader(sucursales)
                for sucursal in reader:
                    if (sucursal[0] == id):
                        print(sucursal)
