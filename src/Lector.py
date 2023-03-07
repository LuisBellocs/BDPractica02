import csv

class Lector:

    @staticmethod
    def encuentra_fila_entidad(cadenaEntidad, id):
        """
        Busca la fila correspondiente a una entidad y la devuelve.

        Parameter
        ---------
        cadenaEntidad : str
            Tipo de entidad a buscar.

        id : str
            ID de la entidad a buscar.

        Returns
        ---------
        dato : str
            Entidad y sus datos.
        """
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
        """
        Decide en qué entidad se debe buscar.

        Parameter
        ---------
        entidad : str
            Código de la entidad.

        id : str
            ID de la entidad a buscar.

        Returns
        ---------
        str
            Entidad y sus datos.
        """
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
        """
        Imprime los datos de una entidad con formato legible.

        Parameter
        ---------
        entidad : str
            Tipo de entidad a imprimir.

        id : str
            ID de la entidad a imprimir.
        """
        datos = Lector.lee(entidad, id)
        if(datos == ""):
            return ""
        if (entidad == 1):
            print("---- Datos del empleado ----")
            print(f"CURP: {datos[0]}")
            print(f"Nombre: {datos[1]}")
            print(f"Direccion: {datos[2]}")
            print("Correo(s) electrónico(s):")
            correos = datos[3].split(";")
            for correo in correos:
                print(correo)
            print("Número(s) de teléfono:")
            numeros = datos[4].split(";")
            for numero in numeros:
                print(numero)
            print(f"Fecha de nacimiento: {datos[5]}")
            print(f"ID sucursal donde trabaja: {datos[6]}")
            print(f"Cargo: {datos[7]}")
        elif (entidad == 2):
            print("---- Datos del producto ----")
            print(f"ID Producto: {datos[0]}")
            print(f"Precio: {datos[1]}")
            print(f"Cantidad total: {datos[2]}")
            print(f"Nombre: {datos[3]}")
            print(f"Marca: {datos[4]}")
            print(f"Número de tiendas con el producto: {datos[5]}")
            print("Stock diponible por tienda:")
            stock = datos[6].split(";")
            for cantidad in stock:
                if(len(cantidad) < 3):
                    continue
                tienda = cantidad.split(":")
                print(f"Tienda: {tienda[0]} Cantidad: {tienda[1]}")
            print(f"Requiere refrigeración: {datos[7]}")
            print(f"Fecha de preparación: {datos[8]}")
            print(f"Fecha de caducidad: {datos[9]}")
        else:
            print("---- Datos de la sucursal ----")
            print(f"ID: {datos[0]}")
            print(f"Nombre: {datos[1]}")
            print(f"Dirección: {datos[2]}")
            print("Número(s) de teléfono:")
            numeros = datos[3].split(";")
            for numero in numeros:
                print(numero)
            print(f"Fecha de apertura: {datos[4]}")
        
