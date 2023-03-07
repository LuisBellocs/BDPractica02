import csv
import sys
import datetime
from Lector import Lector

class Producto:

    debe_editar = False

    @staticmethod
    def agrega():
        """
        Abre el archivo csv en el que se guarda la información y escribe los 
        datos del producto.
        """
        productos = open('productos.csv', 'a')
        with productos:
            writer = csv.writer(productos, delimiter='æ')
            writer.writerow(Producto.get_datos())
            
        productos.close()
    
    @staticmethod
    def edita(id):
        """
        Indica que el producto debe editarse.

        Parameter
        ---------
        id : str
            ID del prodcuto.
        """
        Producto.debe_editar = True
        Producto.decide_edita_elimina(id)
    
    @staticmethod
    def elimina(id):
        """
        Indica que el producto debe eliminarse.

        Parameter
        ---------
        id : str
            ID del producto.
        """
        Producto.debe_editar = False
        Producto.decide_edita_elimina(id)

    @staticmethod
    def decide_edita_elimina(id):
        """
        Elimina o edita el producto correspondiente al ID que recibe.
        En caso de no hallarlo, imprime un mensaje indicando que no se
        encontró en el archivo.

        Parameter
        ---------
        id : str
            ID del producto.
        """
        listaProductos = []
        encontrado = False
        with open('productos.csv', 'r+') as productos:
                reader = csv.reader(productos, delimiter='æ')
                writer = csv.writer(productos, delimiter='æ')
                for producto in reader:
                    if(producto[0] == id):
                        encontrado = True
                    if (producto[0] == id and Producto.debe_editar):
                        listaProductos.append(Producto.get_datos())
                    if (producto[0] != id):
                        listaProductos.append(producto)

        if(encontrado == False):
            print("No se encontró el ID del producto")
        else:
            print("Operación completada con éxito")

        nuevosProductos = open('productos.csv', 'w')
        with nuevosProductos:
            writer = csv.writer(nuevosProductos, delimiter='æ')
            writer.writerows(listaProductos)

    @staticmethod
    def get_datos():
        """
        Junta los datos de un producto y los coloca en un arreglo.

        Returns
        ---------
        array
            Datos del producto.
        """
        id = Producto.checarID()
        precio = Producto.checarPrecio()
        cantidad = Producto.checarInt("Cantidad")
        nombre = input("Nombre: \n")
        marca = input("Nombre de la marca: \n")
        tiendas = Producto.checarInt("Número de tiendas con el producto")
        stock = ""
        for i in range(0,tiendas):
            stock += Producto.checarSucursal(i+1)
            stock += ":"
            stock += str(Producto.checarInt(f"Cantidad en la tienda {i+1}"))
            stock += ";"
        refrigeracion = Producto.checarRefrigeracion()
        preparación = Producto.checarFecha("preparación")
        caducidad = Producto.checarFecha("caducidad")
        return [id, precio, cantidad, nombre, marca, tiendas, 
            stock, refrigeracion, preparación, caducidad]       
        
    @staticmethod
    def checarID():
        """
        Lee el ID del producto; verifica su formato y que no esté repetida.

        Returns
        ---------
        id : str
            ID del producto.
        """
        id = -1
        while(id == -1):
            try:
                id = input("código de producto: \n")
                numid = int(id)
                if(numid < 0):
                    print("ID inválido, intente de nuevo.")
                    id = -1
                else:
                    repetido = Lector.lee(2, id)
                    if(repetido != "" and repetido[0] == id and
                        Producto.debe_editar == False):
                        print("Ya existe un producto con ese código, intente de nuevo.")
                        id = -1
            except:
                print("El código de producto debe ser numérico.")
                id = -1
        return id

    @staticmethod
    def checarFecha(str):
        """
        Lee fechas y verifica su formato.

        Returns
        ---------
        dato : str
            Fecha.
        """
        dato = ""
        while(dato == ""):
            dato = input("Fecha de " + str + " (dd/mm/aaaa): \n")
            numfecha = dato.split("/")
            try:
                fecha = datetime.datetime(int(numfecha[2]), int(numfecha[1]), int(numfecha[0]))
            except:
                print("Formato de fecha inválido, intente de nuevo.")
                dato = ""
        return dato
    
    @staticmethod
    def checarRefrigeracion():
        """
        Lee si requiere o no refigeración el producto.

        Returns
        ---------
        dato : str
            si/no.
        """
        dato = ""
        while(dato == ""):
            dato = input("Requiere refrigeración (si/no): \n")
            dato = dato.lower()
            try:
                if(dato != "si" and dato != "no"):
                    print("Formato inválido, intente de nuevo.")
                    dato = ""
            except:
                print("Formato inválido, intente de nuevo.")
                dato = ""
        return dato
    
    @staticmethod
    def checarPrecio():
        """
        Lee el precio del producto y verifica su formato.

        Returns
        ---------
        dato : str
            Precio del producto.
        """
        dato = -0.1
        while(dato == -0.1):
            try:
                dato = int(input("Precio del de producto: \n"))
                if(dato <= 0):
                    print("Precio inválido, intente de nuevo.")
                    dato = -0.1
            except:
                print("El código de producto debe ser numérico.")
                dato = -0.1
        return dato
    
    @staticmethod
    def checarInt(mensaje):
        """
        Lee y verifica números postivos.

        Returns
        ---------
        dato : str
            Número positivo.
        """
        dato = -1
        while(dato == -1):
            try:
                dato = int(input(f"{mensaje}: \n"))
                if(dato < 0):
                    print("Dato inválido, intente de nuevo.")
                    dato = -1
            except:
                print("Este valor debe de ser numérico, intente de nuevo.")
                dato = -1
        return dato

    @staticmethod
    def checarSucursal(numero):
        """
        Lee el ID de la sucursal en la que se encuentra el producto.

        Returns
        ---------
        id_sucursal : str
            ID de la sucursal en la que se encuentra el producto.
        """
        while (True):
            id_sucursal = input(f"ID de la sucursal {numero}: \n")
            if (not id_sucursal.isdigit()):
                print("La id debe de ser un numero entero positivo")
            elif (not Producto.existe_sucursal(id_sucursal)):
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