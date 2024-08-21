import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """Establece la conexión con la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',  
            user='root',  
            password='',  
            database='concesionario'  # Nombre de la base de datos que creaste
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos Concesionario")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    """Cierra la conexión con la base de datos."""
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

class clientes:
    def __init__(self, id_cliente=None, nombre=None, apellido=None, telefono=None, email=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def agregar(self, conexion):
        """Inserta el cliente en la base de datos."""
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO clientes (nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.nombre, self.apellido, self.telefono, self.email))
            conexion.commit()
            self.id_cliente = cursor.lastrowid
            print("Cliente agregado correctamente")
        except Error as e:
            print(f"Error al agregar cliente: {e}")
        finally:
            cursor.close()

    def editar(self, conexion):
        """Edita los datos del cliente en la base de datos."""
        try:
            cursor = conexion.cursor()
            query = "UPDATE clientes SET nombre = %s, apellido = %s, telefono = %s, email = %s WHERE id_cliente = %s"
            cursor.execute(query, (self.nombre, self.apellido, self.telefono, self.email, self.id_cliente))
            conexion.commit()
            print("Cliente editado correctamente")
        except Error as e:
            print(f"Error al editar cliente: {e}")
        finally:
            cursor.close()

    def borrar(self, conexion):
        """Borra el cliente de la base de datos, eliminando primero los vehículos asociados."""
        try:
            cursor = conexion.cursor()
            # Primero eliminar los vehículos asociados
            query_vehiculos = "DELETE FROM vehiculos WHERE id_cliente = %s"
            cursor.execute(query_vehiculos, (self.id_cliente,))
            
            # Luego eliminar el cliente
            query_cliente = "DELETE FROM clientes WHERE id_cliente = %s"
            cursor.execute(query_cliente, (self.id_cliente,))
            
            conexion.commit()
            print("Cliente borrado correctamente")
        except Error as e:
            print(f"Error al borrar cliente: {e}")
        finally:
            cursor.close()

    @staticmethod
    def obtener_clientes(conexion):
        """Obtiene todos los clientes de la base de datos."""
        try:
            cursor = conexion.cursor()
            query = "SELECT id_cliente, nombre, apellido, telefono, email FROM clientes"
            cursor.execute(query)
            resultado = cursor.fetchall()
            clientes_list = [clientes(id_cliente=row[0], nombre=row[1], apellido=row[2], telefono=row[3], email=row[4]) for row in resultado]
            return clientes_list
        except Error as e:
            print(f"Error al obtener clientes: {e}")
            return []
        finally:
            cursor.close()

class vehiculos:
    def __init__(self, id_vehiculo=None, marca=None, modelo=None, año=None, id_cliente=None):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.id_cliente = id_cliente

    def agregar(self, conexion):
        """Inserta el vehículo en la base de datos."""
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO vehiculos (marca, modelo, año, id_cliente) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.marca, self.modelo, self.año, self.id_cliente))
            conexion.commit()
            self.id_vehiculo = cursor.lastrowid
            print("Vehículo agregado correctamente")
        except Error as e:
            print(f"Error al agregar vehículo: {e}")
        finally:
            cursor.close()

    def editar(self, conexion):
        """Edita los datos del vehículo en la base de datos."""
        try:
            cursor = conexion.cursor()
            query = "UPDATE vehiculos SET marca = %s, modelo = %s, año = %s, id_cliente = %s WHERE id_vehiculo = %s"
            cursor.execute(query, (self.marca, self.modelo, self.año, self.id_cliente, self.id_vehiculo))
            conexion.commit()
            print("Vehículo editado correctamente")
        except Error as e:
            print(f"Error al editar vehículo: {e}")
        finally:
            cursor.close()

    def borrar(self, conexion):
        """Borra el vehículo de la base de datos."""
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM vehiculos WHERE id_vehiculo = %s"
            cursor.execute(query, (self.id_vehiculo,))
            conexion.commit()
            print("Vehículo borrado correctamente")
        except Error as e:
            print(f"Error al borrar vehículo: {e}")
        finally:
            cursor.close()

    @staticmethod
    def obtener_vehiculos(conexion):
        """Obtiene todos los vehículos de la base de datos."""
        try:
            cursor = conexion.cursor()
            query = "SELECT id_vehiculo, marca, modelo, año, id_cliente FROM vehiculos"
            cursor.execute(query)
            resultado = cursor.fetchall()
            vehiculos_list = [vehiculos(id_vehiculo=row[0], marca=row[1], modelo=row[2], año=row[3], id_cliente=row[4]) for row in resultado]
            return vehiculos_list
        except Error as e:
            print(f"Error al obtener vehículos: {e}")
            return []
        finally:
            cursor.close()

def menu():
    conexion = crear_conexion()

    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestionar Clientes")
        print("2. Gestionar Vehículos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            gestionar_clientes(conexion)
        elif opcion == '2':
            gestionar_vehiculos(conexion)
        elif opcion == '3':
            cerrar_conexion(conexion)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_clientes(conexion):
    while True:
        print("\n=== Gestión de Clientes ===")
        print("1. Agregar Cliente")
        print("2. Editar Cliente")
        print("3. Borrar Cliente")
        print("4. Ver Clientes")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            cliente_instance = clientes(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            cliente_instance.agregar(conexion)

        elif opcion == '2':
            id_cliente = input("ID del Cliente a editar: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            telefono = input("Nuevo Teléfono: ")
            email = input("Nuevo Email: ")
            cliente_instance = clientes(id_cliente=id_cliente, nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            cliente_instance.editar(conexion)

        elif opcion == '3':
            id_cliente = input("ID del Cliente a borrar: ")
            cliente_instance = clientes(id_cliente=id_cliente)
            cliente_instance.borrar(conexion)

        elif opcion == '4':
            clientes_list = clientes.obtener_clientes(conexion)
            for cliente in clientes_list:
                print(cliente.id_cliente, cliente.nombre, cliente.apellido, cliente.telefono, cliente.email)

        elif opcion == '5':
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_vehiculos(conexion):
    while True:
        print("\n=== Gestión de Vehículos ===")
        print("1. Agregar Vehículo")
        print("2. Editar Vehículo")
        print("3. Borrar Vehículo")
        print("4. Ver Vehículos")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            año = input("Año: ")
            id_cliente = input("ID del Cliente propietario: ")
            vehiculo_instance = vehiculos(marca=marca, modelo=modelo, año=año, id_cliente=id_cliente)
            vehiculo_instance.agregar(conexion)

        elif opcion == '2':
            id_vehiculo = input("ID del Vehículo a editar: ")
            marca = input("Nueva Marca: ")
            modelo = input("Nuevo Modelo: ")
            año = input("Nuevo Año: ")
            id_cliente = input("Nuevo ID del Cliente propietario: ")
            vehiculo_instance = vehiculos(id_vehiculo=id_vehiculo, marca=marca, modelo=modelo, año=año, id_cliente=id_cliente)
            vehiculo_instance.editar(conexion)

        elif opcion == '3':
            id_vehiculo = input("ID del Vehículo a borrar: ")
            vehiculo_instance = vehiculos(id_vehiculo=id_vehiculo)
            vehiculo_instance.borrar(conexion)

        elif opcion == '4':
            vehiculos_list = vehiculos.obtener_vehiculos(conexion)
            for vehiculo in vehiculos_list:
                print(vehiculo.id_vehiculo, vehiculo.marca, vehiculo.modelo, vehiculo.año, vehiculo.id_cliente)

        elif opcion == '5':
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
