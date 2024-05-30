a=(float(input("Ingresa el primer promedio:")))
b=(float(input("Ingresa el Segundo promedio:")))
c=(float(input("Ingresa el Tercer promedio:")))

if a > b and a > c:
    print("El promedio mayor es:",a)
elif b > a and b > c:
    print("El promedio mayor es:",b)
elif c > a and c > b:
    print("El promedio mayor es:",c)
else:
    print("Los numeros son iguales")
    
    
