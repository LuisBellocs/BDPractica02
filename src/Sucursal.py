import csv

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
        Sucursal.selimina_o_edita(id)            

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
        id = input("código de sucursal: \n")
        nombre = input("Nombre: \n")
        direccion = input("Dirección: \n")
        telefonos = input("Números de teléfono (separados por ';'): \n")
        apertura = input("Fecha de apertura (dd/mm/aaaa): \n")
        return [id, nombre, direccion, telefonos, apertura]
        
