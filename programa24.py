#CLASE////////////////////////////////////////////////////////////////////////
class Auto:
    def __init__(self, marca, tipo, modelo, año):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.año = año
        
    def encender(self):
        print("BRUMMMMM BRUMMMMM")
        
    def avanzar(self):
        print("RUNNNNNNN")
        
    def descripcion(self):
        print ("Es un auto", self.marca,
               "es un", self.tipo, 
               "modelo", 
               self.modelo, self.año)
      
#AGREGACION///////////////////////////////////////////////////////////////////      
class Propietario:
    def __init__(self, nombre):
        self.nombre =nombre
        self.autos = []
        
    def comprar_auto(self, auto):
        self.autos.append(auto)
        print(auto.marca, auto.modelo,"fue comprado por:", self.nombre)
        
    def manejar_auto(self, auto):
        print(self.nombre, "esta manejando un auto:",auto.marca)
        auto.avanzar()
            
    def modificar_auto(self, auto):
             print (self.nombre, "a modificado el auto:",auto.modelo)
 
 
#OBJETOS   
auto1 = Auto("Chevrolet", "Muscle Car","Camaro ZL1","2024")
auto2 = Auto("Toyota", "4X4", "Tacoma","2025")
auto3= Auto("Porche", "Hyper Car", "911 Carrera","2023")

dueño = Propietario ("Emiliano")

#METODOS
dueño.comprar_auto(auto1)
dueño.comprar_auto(auto2)

dueño.manejar_auto(auto3)
dueño.modificar_auto(auto3)

print(auto3.marca)
print(auto2.marca,auto2.modelo,auto2.tipo)
print(auto1.marca,auto1.modelo,auto1.tipo)

auto1.encender()
auto2.avanzar()
auto3.descripcion()