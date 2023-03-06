import csv
import datetime
from Lector import Lector

class Producto:

    debe_editar = False

    @staticmethod
    def agrega():
        productos = open('productos.csv', 'a')
        with productos:
            writer = csv.writer(productos, delimiter='æ')
            writer.writerow(Producto.get_datos())
            
        productos.close()
    
    @staticmethod
    def edita(id):
        Producto.debe_editar = True
        Producto.decide_edita_elimina(id)
    
    @staticmethod
    def elimina(id):
        Producto.debe_editar = False
        Producto.decide_edita_elimina(id)

    @staticmethod
    def decide_edita_elimina(id):
        listaProductos = []
        with open('productos.csv', 'r+') as productos:
                reader = csv.reader(productos, delimiter='æ')
                writer = csv.writer(productos, delimiter='æ')
                existe = False
                for producto in reader:
                    if (producto[0] == id and Producto.debe_editar):
                        listaProductos.append(Producto.get_datos())
                        existe = True
                    if (producto[0] != id):
                        listaProductos.append(producto)
                if (not existe):
                    print(f"No se encontraron productos con el ID {id}")

        nuevosProductos = open('productos.csv', 'w')
        with nuevosProductos:
            writer = csv.writer(nuevosProductos, delimiter='æ')
            writer.writerows(listaProductos)

    @staticmethod
    def get_datos():
        id = Producto.checarID()
        precio = Producto.checarPrecio()
        cantidad = Producto.checarInt("Cantidad")
        nombre = input("Nombre: \n")
        marca = input("Nombre de la marca: \n")
        tiendas = Producto.checarInt("Número de tiendas con el producto")
        stock = ""
        for i in range(0,tiendas):
            stock += input("Nombre de la tienda {}: \n".format(i+1))
            stock += ":"
            stock += str(Producto.checarInt(f"Cantidad en la tienda {i+1}"))
        refrigeracion = Producto.checarRefrigeracion()
        preparación = Producto.checarFecha("preparación")
        caducidad = Producto.checarFecha("caducidad")
        return [id, precio, cantidad, nombre, marca, tiendas, 
            stock, refrigeracion, preparación, caducidad]       
        
    @staticmethod
    def checarID():
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