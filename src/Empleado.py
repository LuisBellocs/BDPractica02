import csv
import sys
import datetime
from Lector import Lector

class Empleado:

    debe_editarse = False
    
    @staticmethod
    def agrega():
        """
        Abre el archivo csv en el que se guarda la información y escribe los 
        datos del empleado.
        """
        empleados = open('empleados.csv', 'a')
        with empleados:
            writer = csv.writer(empleados, delimiter='æ')
            writer.writerow(Empleado.get_datos())
        empleados.close()

        
    @staticmethod
    def edita(id):
        """
        Indica que el empleado debe editarse.

        Parameter
        ---------
        id : str
            ID del empleado.
        """
        Empleado.debe_editarse = True
        Empleado.elimina_o_edita(id)
            
    @staticmethod
    def elimina(id):
        """
        Indica que el empleado debe eliminarse.

        Parameter
        ---------
        id : str
            ID del empleado.
        """
        Empleado.debe_editarse = False
        Empleado.elimina_o_edita(id)

    @staticmethod
    def elimina_o_edita(id):
        """
        Elimina o edita el empleado correspondiente al ID que recibe.
        En caso de no hallarlo, imprime un mensaje indicando que no se
        encontró en el archivo.

        Parameter
        ---------
        id : str
            ID del empleado.
        """
        listaEmpleados = []
        encontrado = False
        with open('empleados.csv', 'r+') as empleados:
            reader = csv.reader(empleados, delimiter='æ')
            writer = csv.writer(empleados, delimiter='æ')
            for empleado in reader:
                if(empleado[0] == id):
                    encontrado = True
                if (empleado[0] == id and Empleado.debe_editarse):
                    listaEmpleados.append(Empleado.get_datos())
                if (empleado[0] != id):
                    listaEmpleados.append(empleado)

        if(encontrado == False):
            print("No se encontró el CURP del empleado")
        else:
            print("Operación completada con éxito")

        nuevosEmpleados = open('empleados.csv', 'w')
        with nuevosEmpleados:
            writer = csv.writer(nuevosEmpleados, delimiter='æ')
            writer.writerows(listaEmpleados)

    @staticmethod
    def get_datos():
        """
        Junta los datos en un empleado y los coloca en un arreglo.

        Returns
        ---------
        array
            Datos del empleado.
        """
        curp = Empleado.checarCurp()
        nombre = Empleado.checarNombre()
        direccion = input("Dirección: \n")
        correos = Empleado.checarEmail()
        celulares = Empleado.checarTel()
        nacimiento = Empleado.checarFecha()
        sucursal = Empleado.checarSucursal()
        cargo = Empleado.checarCargo()
        return [curp, nombre, direccion, correos,
                celulares, nacimiento, sucursal, cargo]
    
    @staticmethod
    def checarCurp():
        """
        Lee la CURP del usuario; verifica su formato y que no esté repetida.

        Returns
        ---------
        curp : str
            CURP del empleado.
        """
        curp = ""
        while (curp == ""):
            curp = input("Ingrese su CURP: ")
            
            if len(curp) != 18:
                print("La CURP debe tener 18 caracteres.")
                curp = ""
                continue
            
            for i in range(18):
                c = curp[i]
                if(i < 4 or (i >= 10 and i <= 16)):                    
                    if not c.isalpha() or not c.isupper():
                        print("La CURP debe contener letras mayúsculas en las posiciones 1, 2, 3, 4 y 11.")
                        curp = ""
                        break
                elif(i == 10):
                    if c != 'H' and c != 'M':
                        print("La CURP debe contener H o M en la posicíon 11.")
                        curp = ""
                        break
                else:
                    if(not c.isdigit()):
                        print("Los caracteres del 5 al 10 y el 18 deben de ser números.")
                        curp = ""
                        break

            repetido = Lector.lee(1, curp)
            if(repetido != "" and repetido[0] == curp):
                print("Ya existe un empleado con ese CURP, intente de nuevo.")
                curp = ""
                continue

        return curp
    
    @staticmethod
    def checarFecha():
        """
        Lee la fecha de nacimiento del usuario y verifica su formato.

        Returns
        ---------
        dato : str
            Fecha de nacimiento del empleado.
        """
        dato = ""
        while(dato == ""):
            dato = input("Fecha de nacimiento (dd/mm/aaaa): \n")
            numfecha = dato.split("/")
            try:
                fecha = datetime.datetime(int(numfecha[2]), int(numfecha[1]), int(numfecha[0]))
            except:
                print("Formato de fecha inválido, intente de nuevo.")
                dato = ""
        return dato
    
    @staticmethod
    def checarTel():
        """
        Lee los teléfonos del usuario y verifica su formato.

        Returns
        ---------
        dato : str
            Teléfonos del empleado.
        """
        dato = ""
        while(dato == ""):
            dato = input("Número(s) de teléfono (separados por ';'): \n")
            telefonos = dato.split(";")
            for numero in telefonos:
                if(len(numero) < 7):
                    print("Los números deben contener al menos 7 dígitos, intente de nuevo.")
                    dato = ""
                    break
                try:
                    num = int(numero)
                except:
                    print("Alguno de los datos es inválido, intente de nuevo.")
                    dato = ""
        return dato
    
    @staticmethod
    def checarEmail():
        """
        Lee los correos del usuario y verifica su formato.

        Returns
        ---------
        dato : str
            Correos del empleado.
        """
        dato = ""
        while(dato == ""):
            dato = input("Correo(s) electrónico(s) (separados por ';'): \n")
            emails = dato.split(";")
            for email in emails:
                if((len(email) < 3) or ("@" not in email) or (email[0] == "@") or (email[-1] == "@")):
                    print("Alguno de los datos es inválido, intente de nuevo.")
                    dato = ""
                
        return dato
    
    @staticmethod
    def checarNombre():
        """
        Lee el nombre del usuario y verifica su formato.

        Returns
        ---------
        nombre : str
            Combre completo del empleado.
        """
        while True:
            nombre = input("Nombre completo (al menos un nombre y un apellido): ")
            if(all(c.isalpha() or c.isspace() for c in nombre) and len(nombre) > 2 and " " in nombre and (nombre[1] != " ") and (nombre[-1] != " ")):
                return nombre
            else:
                print("El formato del nombre es incorrecto, intente de nuevo.")

    @staticmethod
    def checarSucursal():
        """
        Lee el ID de la sucursal en la que trabaja el empleado.

        Returns
        ---------
        id_sucursal : str
            ID de la sucursal en la que trabaja el empleado.
        """
        while (True):
            id_sucursal = input("Agrega la id de la sucursal: \n")
            if (not id_sucursal.isdigit()):
                print("La id debe de ser un numero entero positivo")
            elif (not Empleado.existe_sucursal(id_sucursal)):
                print("Dicha sucursal no existe")
            else:
                return id_sucursal

    @staticmethod
    def existe_sucursal(id_sucursal):
        """
        Verifica si existe la sucursal.

        Paramater
        ---------
        id_sucursal : str
            ID de la sucursal

        Returns
        ---------
        Boolean
            Verdadero si y solo si existe la sucursal.
        """
        try:
            with open('sucursales.csv', 'r+') as sucursales:
                reader = csv.reader(sucursales, delimiter='æ')
                for sucursal in reader:
                    if (sucursal[0] == id_sucursal):
                        return True
        except:
            print("El archivo sucursales.csv no pudo ser encontrado.")
            sys.exit(0)
        return False

    @staticmethod
    def checarCargo():
        """
        Lee el cargo que tiene el empleado.

        Returns
        ---------
        cargos[i] : int
            Cargo del empleado.
        """
        while (True):
            cargo = input("Ingresa el cargo (numero): [1] Gerente, [2] Encargado, [3] Cajero: ")
            if (cargo.isdigit() and int(cargo) > 0 and int(cargo) < 4):
                cargos = ["Gerente", "Encargado", "Cajero"]
                return cargos[int(cargo)-1]
            print("Solo enteros positivos de las opciones enlistadas.")
            
