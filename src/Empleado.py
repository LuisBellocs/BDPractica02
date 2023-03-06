import csv
import datetime

class Empleado:

    debe_editarse = False
    
    @staticmethod
    def agrega():
        empleados = open('empleados.csv', 'a')
        with empleados:
            writer = csv.writer(empleados, delimiter=',')
            writer.writerow(Empleado.get_datos())
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
                    listaEmpleados.append(Empleado.get_datos())
                if (empleado[0] != id):
                    listaEmpleados.append(empleado)

        nuevosEmpleados = open('empleados.csv', 'w')
        with nuevosEmpleados:
            writer = csv.writer(nuevosEmpleados)
            writer.writerows(listaEmpleados)

    @staticmethod
    def get_datos():
        curp = Empleado.checarCurp()
        nombre = Empleado.checarNombre()
        direccion = input("Dirección: \n")
        correos = Empleado.checarEmail()
        celulares = Empleado.checarTel()
        nacimiento = Empleado.checarFecha()
        sucursal = input("Agrega Sucursal: \n") #Implementar la imposibilidad de tener un empleado en dos sucursales
        return [curp, nombre, direccion, correos,
                celulares, nacimiento, sucursal]
        

    def checarCurp():
        while True:
            curp = input("Ingrese su CURP: ")
            
            if len(curp) != 18:
                print("La CURP debe tener 18 caracteres.")
                continue
            
            for i in range(18):
                c = curp[i]
                if(i < 4 or (i >= 10 and i <= 16)):                    
                    if not c.isalpha() or not c.isupper(): # letras mayúsculas
                        print("La CURP debe contener letras mayúsculas en las posiciones 1, 2, 3, 4 y 11.")
                        break
                elif(i == 10):
                    if c != 'H' and c != 'M':
                        print("La CURP debe contener H o M en la posicíon 11.")
                        break
                else:
                    if(not c.isdigit()):
                        print("Los caracteres del 5 al 10 y el 18 deben de ser números")
                        break
            else:
                return curp
            
    def checarFecha():
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
    
    def checarTel():
        dato = ""
        while(dato == ""):
            dato = input("Número(s) de teléfono (separados por ';'): \n")
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
    
    def checarEmail():
        dato = ""
        while(dato == ""):
            dato = input("Correo(s) electríonico(s) (separados por ';'): \n")
            emails = dato.split(";")
            for email in emails:
                if((len(email) < 3) or ("@" not in email) or (email[1] == "@") or (email[-1] == "@")):
                    print("Alguno de los datos es inválido, intente de nuevo.")
                    dato = ""
                
        return dato
    
    def checarNombre():
        while True:
            nombre = input("Nombre completo: ")
            if(all(c.isalpha() or c.isspace() for c in nombre) and len(nombre) > 2 and " " in nombre and (nombre[1] != " ") and (nombre[-1] != " ")):
                return nombre
            else:
                print("El formato del nombre es incorrecto. Inténtelo de nuevo.")
