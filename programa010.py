numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
    
suma = numero1 + numero2
    
print(f"La suma de sus números es {suma}") 

while True:
    continuar = str(input('\n¿Desea continuar sumando los números ingresados? ("si" para continuar |"n" para salir): '))
    
    if continuar == "si": 
        numero1 = float(input("Ingrese un número: "))
        numero2 = float(input("Ingrese otro número: "))
    
        suma = numero1 + numero2
    
        print(f"La suma de sus números es: {suma}") 
        
    elif continuar == "n":
        print("Saliendo....")
        break
    
    