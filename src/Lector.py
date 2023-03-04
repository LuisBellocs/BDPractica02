import csv

class Lector:

    @staticmethod
    def imprime_fila_entidad(cadenaEntidad, id):
        with open(f'{cadenaEntidad}.csv') as entidad:
            reader = csv.reader(entidad) 
            for fila in reader:
                if (fila[0] == id):
                    print(fila)
    
    @staticmethod
    def lee(entidad, id):
        cadenaEntidad = ""
        if (entidad == 1):
            cadenaEntidad = "empleados"
        elif (entidad == 2):
            cadenaEntidad = "productos"
        else:
            cadenaEntidad = "sucursales"
        Lector.imprime_fila_entidad(cadenaEntidad, id)
        
