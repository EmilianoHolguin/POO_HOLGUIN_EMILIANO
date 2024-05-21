print("Bienvenido")
peso= float(input("Ingresa el peso del paquete en Kg, para definir el costo de envio: "))

if peso < 1:
    print("El precio a pagar son $50")
elif peso < 5: 
    print("El precio a pagar son $100")
elif peso < 10: 
    print("El precio a pagar son $200")
elif peso >= 10:
    print("El precio a pagar son $500")
else: 
    print("Por favor ingresa un numero valido")