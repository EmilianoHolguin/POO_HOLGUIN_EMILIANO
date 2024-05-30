productos = {
    "Agua" : 20,
    "Cafe" : 30,
    "Leche" : 28,
    "Huevos" : 56,
    "Pan" : 10,
    "Jamon" : 45,
    "Atun" : 20
}

for cosa in productos:
    precio=productos[cosa]
    
for valor in productos.values():
   descuento= 0.10
   precio= valor -(valor * descuento)
   print(cosa,":$",precio)
   
   