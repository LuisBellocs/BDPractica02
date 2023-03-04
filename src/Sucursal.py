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
        listaSucursales = []
        with open('sucursales.csv', 'r+') as sucursales:
                reader = csv.reader(sucursales)
                writer = csv.writer(sucursales, delimiter=',')
                for sucursal in reader:
                    if (sucursal[0] == id):
                        id = input("código de sucursal: \n")
                        nombre = input("Nombre: \n")
                        direccion = input("Dirección: \n")
                        telefonos = input("Números de teléfono (separados por ';'): \n")
                        apertura = input("Fecha de apertura (dd/mm/aaaa): \n")
                        listaSucursales.append([id, nombre, direccion,
                            telefonos, apertura])
                    else:
                        listaSucursales.append(sucursal)

        nuevasSucursales = open('sucursales.csv', 'w')
        with nuevasSucursales:
            writer = csv.writer(nuevasSucursales)
            writer.writerows(listaSucursales)
    
    @staticmethod
    def elimina(id):
        listaSucursales = []
        with open('sucursales.csv', 'r+') as sucursales:
                reader = csv.reader(sucursales)
                writer = csv.writer(sucursales, delimiter=',')
                for sucursal in reader:
                    if (sucursal[0] != id):
                        listaSucursales.append(sucursal)

        nuevasSucursales = open('sucursales.csv', 'w')
        with nuevasSucursales:
            writer = csv.writer(nuevasSucursales)
            writer.writerows(listaSucursales)
            
            