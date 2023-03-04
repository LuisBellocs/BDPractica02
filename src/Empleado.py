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
        listaEmpleados = []
        with open('empleados.csv', 'r+') as empleados:
                reader = csv.reader(empleados)
                writer = csv.writer(empleados, delimiter=',')
                for empleado in reader:
                    if (empleado[0] == id):
                        curp = input("CURP: \n")
                        nombre = input("Nombre: \n")
                        direccion = input("Dirección: \n")
                        correos = input("Correos (separados por ';'): \n")
                        celulares = input("Números de celular (separados por ';'): \n")
                        nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): \n")
                        listaEmpleados.append([curp, nombre, direccion, correos,
                            celulares, nacimiento])
                    else:
                        listaEmpleados.append(empleado)

        nuevosEmpleados = open('empleados.csv', 'w')
        with nuevosEmpleados:
            writer = csv.writer(nuevosEmpleados)
            writer.writerows(listaEmpleados)
    @staticmethod
    def elimina(id):
        listaEmpleados = []
        with open('empleados.csv', 'r+') as empleados:
                reader = csv.reader(empleados)
                writer = csv.writer(empleados, delimiter=',')
                for empleado in reader:
                    if (empleado[0] != id):
                        listaEmpleados.append(empleado)

        nuevosEmpleados = open('empleados.csv', 'w')
        with nuevosEmpleados:
            writer = csv.writer(nuevosEmpleados)
            writer.writerows(listaEmpleados)
