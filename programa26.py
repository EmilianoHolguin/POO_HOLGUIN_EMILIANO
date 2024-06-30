#CLASE////////////////////////////////////////////////////////////////////////
class Auto:
    def __init__(self, marca, tipo, modelo, año):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.año = año
        self.interior = None
        
    def encender(self):
        print("BRUMMMMM BRUMMMMM")
        
    def avanzar(self):
        print("RUNNNNNNN")
        
    def elegir_interior(self, interior):
        self.interior = interior
        
    def descripcion(self):
        print ("Es un auto", self.marca,
               "es un", self.tipo, 
               "modelo", 
               self.modelo, self.año)
        if self.interior:
            print("Los interiores del auto son de", 
              self.interior.material, "y de color", self.interior.color)
        
#ASOCIACION///////////////////////////////////////////////////////////////////
class Mecanico:
    def __init__(self,nombre):
        self.nombre = nombre
        self.auto_reparado = []
        
    def reparar_auto(self, auto):
        if auto not in self.auto_reparado:
            self.auto_reparado.append(auto)
            print ("El Mecanico",self.nombre,"esta reparando el vehiculo:",auto.modelo)
        else:
            print("El Mecanico",self.nombre,"a repardo el vehiculo:",auto.modelo)
            
    def autos_reparados(self):
        print (self.nombre,"el Mecanico a repardo los sig vehiculos:")
        for auto in self.auto_reparado:
            print(auto.modelo)
            
      
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
 
#COMPOSICION//////////////////////////////////////////////////////////////////
class Interior:
    def __init__(self, material, color):
        self.material = material
        self.color = color  
        
    def descripcion(self):
        print("Los interiores del auto son de", 
              self.material, "y de color", self.color)
    
#OBJETOS
auto1 = Auto("Chevrolet", "Muscle Car","Camaro ZL1","2024")
auto2 = Auto("Toyota", "4X4", "Tacoma","2025")
auto3= Auto("Porche", "Hyper Car", "911 Carrera","2023")

dueño = Propietario ("Emiliano")
mecanico = Mecanico ("Mr. Alan")

interior1 = Interior("Alcantar","Negro con rojo")
interior2 = Interior("Piel", "Cafe")
interior3 = Interior("Tela","Negro")

#METODOS
dueño.comprar_auto(auto1)
dueño.comprar_auto(auto2)

auto1.elegir_interior(interior1)
auto2.elegir_interior(interior3)
auto3.elegir_interior(interior2)

mecanico.reparar_auto(auto2)
mecanico.autos_reparados()

dueño.manejar_auto(auto3)
dueño.modificar_auto(auto3)

print(auto3.marca)
print(auto2.marca,auto2.modelo,auto2.tipo)
print(auto1.marca,auto1.modelo,auto1.tipo)

auto1.encender()
auto2.avanzar()
auto3.descripcion()