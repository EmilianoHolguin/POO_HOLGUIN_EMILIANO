class Auto:
    def __init__(self, marca, tipo, modelo):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        
    def encender(self):
        print("BRUMMMMM BRUMMMMM")
        
    def avanzar(self):
        print("RUNNNNNNN")
    
#OBJETOS
auto1 = Auto("Chevrolet", "Muscle Car","Camaro ZL1")
auto2 = Auto("Toyota", "4X4", "Tacoma")
auto3= Auto("Porche", "Hyper Car", "911 Carrera")

#METODOS
print(auto3.marca)
print(auto2.marca,auto2.modelo,auto2.tipo)
print(auto1.marca,auto1.modelo,auto1.tipo)

auto1.encender()
auto2.avanzar()
