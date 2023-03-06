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
        
