import csv

class Producto:

    @staticmethod
    def agrega():
        productos = open('productos.csv', 'a')
        
        with productos:
            writer = csv.writer(productos, delimiter=',')
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
                reader = csv.reader(productos)
                writer = csv.writer(productos, delimiter=',')
                for producto in reader:
                    if (producto[0] == id and Producto.debe_editar):
                        listaProductos.append(Producto.get_datos())
                    if (producto[0] != id):
                        listaProductos.append(producto)

        nuevosProductos = open('productos.csv', 'w')
        with nuevosProductos:
            writer = csv.writer(nuevosProductos)
            writer.writerows(listaProductos)
        

    @staticmethod
    def get_datos():
        id = input("código de producto: \n")
        precio = input("Precio: \n")
        cantidad = input("Cantidad total de productos: \n")
        nombre = input("Nombre: \n")
        marca = input("Presentación: \n")
        tiendas = int(input("Número de tiendas con el producto: \n"))
        stock = ""
        for i in range(0,tiendas):
            stock += input("Nombre de la tienda {}: \n".format(i+1))
            stock += ":"
            stock += input("Cantidad en la tienda {}: \n".format(i+1))
        refrigeracion = input("Requiere refrigeración (si/no): \n")
        preparación = input("Fecha de preparación o elaboración (dd/mm/aaaa): \n")
        caducidad = input("Fecha de caducidad (dd/mm/aaaa): \n")
        return [id, precio, cantidad, nombre,
                    marca, tiendas, stock, refrigeracion,
                    preparación, caducidad]
