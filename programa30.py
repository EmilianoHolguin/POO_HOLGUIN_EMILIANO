import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="Emiliano Holguin",
    password="Emiliano.2024",
    database="usuario"
)

cursor = conexion.cursor()

cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Alan, 19)")
conexion.commit()  
print("Registro insertado.")

cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

cursor.execute("UPDATE usuarios SET nombre = 'Emiliano' WHERE edad = 21")
conexion.commit()
print("Registro actualizado.")

cursor.execute("DELETE FROM usuarios WHERE edad = 21")
conexion.commit()
print("Registro eliminado.")g

cursor.close()
conexion.close()