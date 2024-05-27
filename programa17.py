while True:
    print("Conversion de temperatura que deseas hacer: ")
    print("a) Celcius a Farenheit")
    print("b) Farenheit a Celcius")
    print("c) Cerrar el programa \n")

    eleccion = str(input())

    if eleccion == "a":
        usuario = float(input("Ingrese los Celsius: \n"))        
        Farenheit = (usuario * 9 / 5) + 32
        print(usuario, "Celsius son", Farenheit, "Fahrenheit")
    
    elif eleccion == "b":
        usuario = float(input("Ingrese los Farenheit: \n"))
        Celcius = (usuario - 32) * 5 / 9
        print(usuario, "Fahrenheit son", Celcius, "Celsius")
    
    elif eleccion == "c":
        print("Saliendo del programa...")
        break
    else:
        print("No ingresaste una opcion dentro del menú")
        print("Ingresa un valor correcto\n")
        
        
        





