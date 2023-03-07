import csv
import datetime
from Lector import Lector

class Sucursal:

    debe_editarse = False
    
    @staticmethod
    def agrega():
        """
        Abre el archivo csv en el que se guarda la información y escribe los 
        datos de la sucursal.
        """
        sucursales = open('sucursales.csv', 'a')
        with sucursales:
            writer = csv.writer(sucursales, delimiter='æ')
            writer.writerow(Sucursal.get_datos())
        
        sucursales.close()
        
    @staticmethod
    def edita(id):
        """
        Indica que la sucursal debe editarse.

        Parameter
        ---------
        id : str
            ID de la sucursal.
        """
        Sucursal.debe_editarse = True
        Sucursal.elimina_o_edita(id)
    
    @staticmethod
    def elimina(id):
        """
        Indica que la sucursal debe eliminarse.

        Parameter
        ---------
        id : str
            ID de la sucursal.
        """
        Sucursal.debe_editarse = False
        Sucursal.elimina_o_edita(id)            

    @staticmethod
    def elimina_o_edita(id):
        listaSucursales = []
        encontrado = False
        with open('sucursales.csv', 'r+') as sucursales:
                reader = csv.reader(sucursales, delimiter='æ')
                writer = csv.writer(sucursales, delimiter='æ')
                for sucursal in reader:
                    if(sucursal[0] == id):
                        encontrado = True
                    if (sucursal[0] == id and Sucursal.debe_editarse):
                        listaSucursales.append(Sucursal.get_datos())
                    if (sucursal[0] != id):
                        listaSucursales.append(sucursal)
        if(encontrado == False):
            print("No se encontró el ID de la Sucursal")
        else:
            print("Operación completada con éxito")

        nuevasSucursales = open('sucursales.csv', 'w')
        with nuevasSucursales:
            writer = csv.writer(nuevasSucursales, delimiter='æ')
            writer.writerows(listaSucursales)

    @staticmethod
    def get_datos():
        """
        Junta los datos de una sucursal y los coloca en un arreglo.

        Returns
        ---------
        array
            Datos de la sucursal.
        """
        id = Sucursal.checarID()
        nombre = input("Nombre: \n")
        direccion = input("Dirección: \n")
        telefonos = Sucursal.checarTel()
        apertura = Sucursal.checarFecha()
        return [id, nombre, direccion, telefonos, apertura]

    @staticmethod
    def checarID():
        """
        Lee el ID de la sucursal; verifica su formato y que no esté repetida.

        Returns
        ---------
        id : str
            ID de la sucursal.
        """
        id = -1
        while(id == -1):
            try:
                id = input("código de sucursal: \n")
                numid = int(id)
                if(numid < 0):
                    print("ID inválido, intente de nuevo.")
                    id = -1
                else:
                    repetido = Lector.lee(3, id)
                    if(repetido != "" and repetido[0] == id and
                        Sucursal.debe_editarse == False):
                        print("Ya existe una sucursal con esa ID, intente de nuevo.")
                        id = -1
            except:
                print("El ID debe ser numérico, intente de nuevo.")
                id = -1
        return id

    @staticmethod
    def checarTel():
        """
        Lee los teléfonos de la sucursal y verifica su formato.

        Returns
        ---------
        dato : str
            Teléfonos de la sucursal.
        """
        dato = ""
        while(dato == ""):
            dato = input("Números de teléfono (separados por ';'): \n")
            telefonos = dato.split(";")
            for numero in telefonos:
                if(len(numero) < 7):
                    print("Alguno de los datos es inválido, intente de nuevo.")
                    dato = ""
                try:
                    num = int(numero)
                except:
                    print("Alguno de los datos es inválido, intente de nuevo.")
                    dato = ""
        return dato

    @staticmethod
    def checarFecha():
        """
        Lee fechas verifica y su formato.

        Returns
        ---------
        dato : str
            Fecha.
        """
        dato = ""
        while(dato == ""):
            dato = input("Fecha de apertura (dd/mm/aaaa): \n")
            numfecha = dato.split("/")
            try:
                fecha = datetime.datetime(int(numfecha[2]), int(numfecha[1]), int(numfecha[0]))
            except:
                print("Formato de fecha inválido, intente de nuevo.")
                dato = ""
        return dato
        

        
