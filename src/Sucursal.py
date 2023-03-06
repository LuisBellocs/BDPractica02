import csv
import datetime
from Lector import Lector

class Sucursal:

    debe_editarse = False
    
    @staticmethod
    def agrega():
        sucursales = open('sucursales.csv', 'a')
    
        with sucursales:
            writer = csv.writer(sucursales, delimiter=',')
            writer.writerow(Sucursal.get_datos())
        
        sucursales.close()
        
    @staticmethod
    def edita(id):
        Sucursal.debe_editarse = True
        Sucursal.elimina_o_edita(id)
    
    @staticmethod
    def elimina(id):
        Sucursal.debe_editarse = False
        Sucursal.elimina_o_edita(id)            

    @staticmethod
    def elimina_o_edita(id):
        listaSucursales = []
        with open('sucursales.csv', 'r+') as sucursales:
                reader = csv.reader(sucursales)
                writer = csv.writer(sucursales, delimiter=',')
                for sucursal in reader:
                    if (sucursal[0] == id and Sucursal.debe_editarse):
                        listaSucursales.append(Sucursal.get_datos())
                    if (sucursal[0] != id):
                        listaSucursales.append(sucursal)

        nuevasSucursales = open('sucursales.csv', 'w')
        with nuevasSucursales:
            writer = csv.writer(nuevasSucursales)
            writer.writerows(listaSucursales)

    @staticmethod
    def get_datos():
        id = Sucursal.checarID()
        nombre = input("Nombre: \n")
        direccion = input("Dirección: \n")
        telefonos = Sucursal.checarTel()
        apertura = Sucursal.checarFecha()
        return [id, nombre, direccion, telefonos, apertura]

    @staticmethod
    def checarID():
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
        

        
