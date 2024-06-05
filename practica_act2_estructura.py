#Objetivo: Practicar el uso de diccionarios y estructuras de control

#Crear un diccionario vacio para almacenar información de los estuduiantes
estudiante = {}
calificaciones = {}
eleccion = ""

#Crear un menu que permita al usario agregar estudiantes con sus calificaciones de un estudiante especifico,
while eleccion != "C": 
    print("Que es lo que deseas hacer hoy: ")
    print("A) Agregar Estudiante y Calificaciones")
    print("B) Visualizar calificaciones")
    print("C) Salir")
    eleccion = str(input())
    eleccion.upper()

    if eleccion.upper() == "A":
        print("Ingrese el nombre completo del estudiante \n empezando por apellidos")
        nombre = str(input())
        while True:
            print("Ingrese el nombre de la materia, Para salir escribir 'fin': ")
            materia = str(input())
            if materia.lower() == "fin":
                break
            calificacion = float(input("Ingrese la calificacion: "))

            calificaciones[materia] = calificacion
            estudiante[nombre] = calificaciones

            print(estudiante)

    elif eleccion == "B":
        nombre = input("Ingrese el nombre del estudiante que quiere consultar: ")

        if nombre in estudiante:
            print(f"{nombre}: {calificaciones}")
            