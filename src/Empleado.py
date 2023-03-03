import csv

class Empleado:

    @staticmethod
    def agrega():
        empleados = open('empleados.csv', 'a')
        
        curp = input("CURP: \n")
        nombre = input("Nombre: \n")
        direccion = input("Dirección: \n")
        correos = input("Correos (separados por ';'): \n")
        celulares = input("Números de celular (separados por ';'): \n")
        nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): \n")
                
        with empleados:
            writer = csv.writer(empleados, delimiter=',')
            writer.writerow([curp, nombre, direccion, correos,
                                                celulares, nacimiento])
        
        empleados.close()

    @staticmethod
    def edita(id):
        empleados = open('empleados.csv')
        with empleados:
            reader = csv.reader(empleados, delimiter = ',')
            close()
                #TODO implementar método

    @staticmethod
    def elimina(id):
        empleados = open('empleados.csv')
        with empleados:
            reader = csv.reader(empleados, delimiter = ',')
            close()
                #TODO implementar método
