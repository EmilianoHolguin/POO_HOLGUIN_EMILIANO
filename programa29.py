def menu():
    print("Seleccione una opción:")
    print("1. Abstracción")
    print("2. Encapsulamiento")
    print("3. Herencia")
    print("4. Polimorfismo")
    print("5. Salir")

def abstraccion():
    print("Abstracción:")
    print("La abstracción es un concepto que permite ocultar los detalles complejos y mostrar solo la funcionalidad esencial del objeto.")
    print("Por ejemplo, cuando usas un coche, no necesitas saber cómo funciona el motor para conducirlo.")

def encapsulamiento():
    print("Encapsulamiento:")
    print("El encapsulamiento es una técnica que consiste en agrupar datos y métodos que operan sobre esos datos en una sola unidad, llamada clase.")
    print("Se logra mediante el uso de modificadores de acceso que controlan el acceso a los datos y métodos dentro de la clase.")

def herencia():
    print("Herencia:")
    print("La herencia es un mecanismo que permite crear una nueva clase a partir de una clase existente.")
    print("La nueva clase, llamada clase derivada, hereda los atributos y métodos de la clase base, permitiendo reutilizar el código y crear una jerarquía de clases.")

def polimorfismo():
    print("Polimorfismo:")
    print("El polimorfismo es la capacidad de un objeto de tomar muchas formas.")
    print("Permite que una misma interfaz se utilice para diferentes tipos de datos, lo que permite que el mismo método o función se comporte de manera diferente según el objeto con el que esté trabajando.")

def main():
    while True:
        menu()
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            abstraccion()
        elif opcion == "2":
            encapsulamiento()
        elif opcion == "3":
            herencia()
        elif opcion == "4":
            polimorfismo()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()