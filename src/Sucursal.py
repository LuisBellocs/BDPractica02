import csv

class Sucursal:

    @staticmethod
    def agrega():
        sucursales = open('sucursales.csv', 'a')
    
        id = input("código de sucursal: \n")
        nombre = input("Nombre: \n")
        direccion = input("Dirección: \n")
        telefonos = input("Números de teléfono (separados por ';'): \n")
        apertura = input("Fecha de apertura (dd/mm/aaaa): \n")

        with sucursales:
            writer = csv.writer(sucursales, delimiter=',')
            writer.writerow([id, nombre, direccion,
                            telefonos, apertura])
        
        sucursales.close()
        
    @staticmethod
    def edita(id):
        sucursales = open("sucursales.csv")
        with sucursales:
            reader = csv.reader(sucursales)
            close()
                #TODO implementar método
    
    @staticmethod
    def elimina(id):
        sucursales = open("sucursales.csv")
        with sucursales:
            reader = csv.reader(sucursales)
            close()
                #TODO implementar método
            
            