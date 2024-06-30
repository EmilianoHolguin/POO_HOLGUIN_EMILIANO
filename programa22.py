def suma (a, b):
    suma= a+b
    return suma

def resta (a,b):
    resta= a-b
    return resta

def multiplicacion (a,b):
    multiplicacion= a*b
    return multiplicacion

def  dividir (a,b):
    dividir= a/b
    return dividir

def calculadora():
    print("SELECCIONA LA OPERACION")
    print("1) SUMA")
    print("2) RESTA")
    print("3) MULTIPLICACION")
    print("4) DIVISION")
    print("5) SALIR DEL PROGRAMA")

    operacion= input("Ingresa el numero de la operacion: ")

    if operacion in {"1","2","3","4"}:
        x =float(input("Ingresa el primer numero:"))
        y =float(input("Ingresa el segundo numero:"))
    
        if operacion == "1":
            print("RESULTADO:", suma(x,y))
        elif operacion == "2":
            print("RESULTADO:", resta(x,y))
        elif operacion == "3":
            print("RESULTADO:", multiplicacion(x,y))
        elif operacion == "4":
            print ("RESULTADO:", dividir(x,y))
    elif operacion in {"5"}:
        print ("Saliendo del programa....")
    else:
        print("Opcion no valida...")
calculadora()
