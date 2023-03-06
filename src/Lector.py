import csv

class Lector:

    @staticmethod
    def encuentra_fila_entidad(cadenaEntidad, id):
        dato = ""
        try:
            with open(f'{cadenaEntidad}.csv') as entidad:
                reader = csv.reader(entidad, delimiter='æ') 
                for fila in reader:
                    if (fila[0] == id):
                        dato = fila
        except:
            print(f"El archivo {cadenaEntidad}.csv no pudo ser encontrado.")
        return dato
        
    
    @staticmethod
    def lee(entidad, id):
        cadenaEntidad = ""
        if (entidad == 1):
            cadenaEntidad = "empleados"
        elif (entidad == 2):
            cadenaEntidad = "productos"
        else:
            cadenaEntidad = "sucursales"
        return Lector.encuentra_fila_entidad(cadenaEntidad, id)


    @staticmethod
    def imprime(entidad, id):
        datos = Lector.lee(entidad, id)
        if(datos == ""):
            return ""
        if (entidad == 1):
            print("Datos del empleado")
            print(f"CURP: {datos[0]}")
            print(f"Nombre: {datos[1]}")
            print(f"Direccion: {datos[2]}")
            print(f"Correo(s) electrónico(s): {datos[3]}")
            print(f"Número(s) de teléfono: {datos[4]}")
            print(f"Fecha de nacimiento: {datos[5]}")
            print(f"ID sucursal donde trabaja: {datos[6]}")
            print(f"Cargo: {datos[7]}")
        elif (entidad == 2):
            print("Datos del Producto")
            print(f"ID Producto: {datos[0]}")
            print(f"Precio: {datos[1]}")
            print(f"Cantidad total: {datos[2]}")
            print(f"Nombre: {datos[3]}")
            print(f"Marca: {datos[4]}")
            print(f"Número de tiendas con el producto: {datos[5]}")
            print(f"Stock diponible: {datos[6]}")
            print(f"Requiere refrigeración: {datos[7]}")
            print(f"Fecha de preparación: {datos[8]}")
            print(f"Fecha de caducidad: {datos[9]}")
        else:
            print("Datos de la sucursal")
            print(f"ID: {datos[0]}")
            print(f"Nombre: {datos[1]}")
            print(f"Dirección: {datos[2]}")
            print(f"Teléfonos: {datos[3]}")
            print(f"Fecha de apertura: {datos[4]}")
        
