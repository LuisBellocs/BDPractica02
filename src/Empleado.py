import csv

class Empleado:

    debe_editarse = False
    
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
        Empleado.debe_editarse = True
        Empleado.elimina_o_edita(id)
            
    @staticmethod
    def elimina(id):
        Empleado.debe_editarse = False
        Empleado.elimina_o_edita(id)

    @staticmethod
    def elimina_o_edita(id):
        listaEmpleados = []
        with open('empleados.csv', 'r+') as empleados:
            reader = csv.reader(empleados)
            writer = csv.writer(empleados, delimiter=',')
            for empleado in reader:
                if (empleado[0] == id and Empleado.debe_editarse):
                    curp = input("CURP: \n")
                    nombre = input("Nombre: \n")
                    direccion = input("Dirección: \n")
                    correos = input("Correos (separados por ';'): \n")
                    celulares = input("Números de celular (separados por ';'): \n")
                    nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): \n")
                    listaEmpleados.append([curp, nombre, direccion, correos,
                                           celulares, nacimiento])
                if (empleado[0] != id):
                    listaEmpleados.append(empleado)

        nuevosEmpleados = open('empleados.csv', 'w')
        with nuevosEmpleados:
            writer = csv.writer(nuevosEmpleados)
            writer.writerows(listaEmpleados)
        
