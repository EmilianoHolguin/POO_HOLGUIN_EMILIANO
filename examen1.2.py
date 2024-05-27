while True:
    print("Que area quieres calcular: ")
    print("a) Cuadrado")
    print("b) Triangulo")
    print("c) Rectangulo")
    print("d) Cerrar el programa \n")

    eleccion = str(input())

    if eleccion == "a":
        usuario = float(input("Ingrese la medida por lado: \n"))        
        Area_C = (usuario * usuario)
        print(Area_C, "Es el area del cuadrado")
    
    elif eleccion == "b":
        usuario1 = float(input("Ingresa la base: \n"))
        usuario2 = float(input("Ingresa la altura: \n"))
        Area_R = (usuario1 * usuario2)
        print(Area_R, "Es el area de tu rectangulo")
        
    elif eleccion == "c":
        usuario3 = float(input("Ingresa la base: \n"))
        usuario4 = float(input("Ingresa la altura: \n"))
        Area_T = (usuario3 * usuario4)/2
        print(Area_T, "Es el area de tu rectangulo")
    
    elif eleccion == "d":
        print("Saliendo del programa...")
        break
    else:
        print("No ingresaste una opcion dentro del menú")
        print("Ingresa un valor correcto\n")