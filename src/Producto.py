import csv

class Producto:

    @staticmethod
    def agrega():
        productos = open('productos.csv', 'a')
        
        id = input("código de producto: \n")
        precio = input("Precio: \n")
        cantidad = input("Cantidad total de productos: \n")
        nombre = input("Nombre: \n")
        marca = input("Presentación: \n")
        tiendas = int(input("Número de tiendas con el producto: \n"))
        stock = ""
        for i in range(0,tiendas):
            stock += input("Nombre de la tienda {}: \n".format(i))
            stock += ":"
            stock += input("Cantidad en la tienda {}: \n".format(i+1))
        refrigeracion = input("Requiere refrigeración (si/no): \n")
        preparación = input("Fecha de preparación o elaboración (dd/mm/aaaa): \n")
        caducidad = input("Fecha de caducidad (dd/mm/aaaa): \n")

        with productos:
            writer = csv.writer(productos, delimiter=',')
            writer.writerow([id, precio, cantidad, nombre,
                    marca, tiendas, stock, refrigeracion,
                    preparación, caducidad])
            
        productos.close()
    
    @staticmethod
    def edita(id):
        productos = open("productos.csv")
        with productos:
            reader = csv.reader(productos, delimiter = ',')
            close()
                #TODO implementar método
    
    @staticmethod
    def elimina(id):
        productos = open("productos.csv")
        with productos:
            reader = csv.reader(productos, delimiter = ',')
            close()
                #TODO implementar método
            