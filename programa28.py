# CLASE ////////////////////////////////////////////////////////////////////////
class Auto:
    def __init__(self, marca, tipo, modelo, año):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.año = año
        self.interior = None
        self.motor = None  
        
    def encender(self):
        print("BRUMMMMM BRUMMMMM")
        if self.motor:
            self.motor.arrancar()
        
    def avanzar(self):
        print("RUNNNNNNN")
        
    def elegir_interior(self, interior):
        self.interior = interior
        
    def agregar_motor(self, motor):
        self.motor = motor
        
    def descripcion(self):
        print ("Es un auto", self.marca,
               "es un", self.tipo, 
               "modelo", 
               self.modelo, self.año)
        if self.interior:
            print("Los interiores del auto son de", 
              self.interior.material, "y de color", self.interior.color)
        if self.motor:
            print("Tiene un motor", self.motor.tipo)

# ASOCIACION ///////////////////////////////////////////////////////////////////
class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.auto_reparado = []
        
    def reparar_auto(self, auto):
        if auto not in self.auto_reparado:
            self.auto_reparado.append(auto)
            print ("El Mecanico", self.nombre, "está reparando el vehículo:", auto.modelo)
        else:
            print("El Mecanico", self.nombre, "ya reparó el vehículo:", auto.modelo)
            
    def autos_reparados(self):
        print(self.nombre, "el Mecanico ha reparado los siguientes vehículos:")
        for auto in self.auto_reparado:
            print(auto.modelo)
      
# AGREGACION ///////////////////////////////////////////////////////////////////
class Propietario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.autos = []
        
    def comprar_auto(self, auto):
        self.autos.append(auto)
        print(auto.marca, auto.modelo, "fue comprado por:", self.nombre)
        
    def manejar_auto(self, auto):
        print(self.nombre, "está manejando un auto:", auto.marca)
        auto.avanzar()
            
    def modificar_auto(self, auto):
        print(self.nombre, "ha modificado el auto:", auto.modelo)
 
# COMPOSICION //////////////////////////////////////////////////////////////////
class Interior:
    def __init__(self, material, color):
        self.material = material
        self.color = color  
        
    def descripcion(self):
        print("Los interiores del auto son de", 
              self.material, "y de color", self.color)
    
# HERENCIA /////////////////////////////////////////////////////////////////////
class AutoDeportivo(Auto):
    def __init__(self, marca, modelo, tipo, año, velocidad_max):
        super().__init__(marca, tipo, modelo, año)
        self.velocidad_max = velocidad_max
        
    def descripcion(self):
        super().descripcion()
        print("El",self.tipo, self.marca, self.modelo, self.año, 
              "tiene una vel. máxima de", self.velocidad_max,
              "km/h, por eso es un auto deportivo.")
        
    def encender(self):
        print("El Auto deportivo está encendido y listo para correr")

# DEPENDENCIA //////////////////////////////////////////////////////////////////
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def arrancar(self):
        print("El motor",self.tipo, "está arrancado.")
        
    def detener(self):
        print("El motor",self.tipo, "está detenido.")

# OBJETOS
motor1 = Motor("6.2L V8")
motor2 = Motor("3.5 L V6 Dual VVT-i")
motor3 = Motor("4.0 L 6-motor bóxer")
motor4 = Motor("V8 M838TQ de 3,8 litros y doble turbocompresor")

auto1 = Auto("Chevrolet", "Muscle Car", "Camaro ZL1", 2024)
auto2 = Auto("Toyota", "4X4", "Tacoma", 2025)
auto3 = Auto("Porsche", "Hyper Car", "911 Carrera", 2023)
auto4 = AutoDeportivo("McLaren", "P1 TM", "Superdeportivo", 2024, 350)

dueño = Propietario("Emiliano")
mecanico = Mecanico("Mr. Alan")

interior1 = Interior("Alcántara", "Negro con rojo")
interior2 = Interior("Piel", "Café")
interior3 = Interior("Tela", "Negro")
interior4 = Interior("Alcantar y Cuero", "Negro y Blanco")

# Métodos
dueño.comprar_auto(auto1)
dueño.comprar_auto(auto2)

auto1.elegir_interior(interior1)
auto2.elegir_interior(interior3)
auto3.elegir_interior(interior2)
auto4.elegir_interior(interior4)

auto1.agregar_motor(motor1)
auto2.agregar_motor(motor2)
auto3.agregar_motor(motor3)
auto4.agregar_motor(motor4)

mecanico.reparar_auto(auto2)
mecanico.autos_reparados()

dueño.manejar_auto(auto3)
dueño.modificar_auto(auto3)

auto4.descripcion()
auto4.encender()
auto1.descripcion()
