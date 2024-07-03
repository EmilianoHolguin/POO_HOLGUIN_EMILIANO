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

# OBJETOS///////////////////////////////////////////////////////////////////////

#MOTOR:
motor1 = Motor("6.2L V8")
motor2 = Motor("3.5 L V6 Dual VVT-i")
motor3 = Motor("4.0 L 6-motor bóxer")
motor4 = Motor("V8 M838TQ de 3,8 litros y doble turbocompresor")

#AUTOS:
auto1 = Auto("Chevrolet", "Muscle Car", "Camaro ZL1", "2024")
auto2 = Auto("Toyota", "4X4", "Tacoma", "2025")
auto3 = Auto("Porsche", "Hyper Car", "911 Carrera", "2023")
auto4 = AutoDeportivo("McLaren", "P1 TM", "Superdeportivo", "2024", "350")

auto1.agregar_motor(motor1)
auto2.agregar_motor(motor2)
auto3.agregar_motor(motor3)
auto4.agregar_motor(motor4)

#PROPIETARIO Y MECANICO:
dueño = Propietario("Emiliano")
mecanico = Mecanico("Mr. Alan")

#INTERIORES:
interior1 = Interior("Alcántara", "Negro con rojo")
interior2 = Interior("Piel", "Café")
interior3 = Interior("Tela", "Negro")
interior4 = Interior("Alcantar y Cuero", "Negro y Blanco")

#MENU/////////////////////////////////////////////////////////////////////////
def menu():
    print("--- MENÚ ---")
    print("1) Comprar auto")
    print("2) Elegir interior del auto")
    print("3) Encender auto")
    print("4) Avanzar con el auto")
    print("5) Reparar auto")
    print("6) Ver autos reparados por el mecánico")
    print("7) Ver descripción del auto")
    print("8) Salir")

def seleccionar_auto():
    print("Seleccione el auto:")
    print("1) Chevrolet Camaro ZL1")
    print("2) Toyota Tacoma")
    print("3) Porsche 911 Carrera")
    print("4) McLaren P1 TM")
    seleccion = (input("Ingrese el número del auto: "))
    if seleccion == "1":
        return auto1
    elif seleccion == "2":
        return auto2
    elif seleccion == "3":
        return auto3
    elif seleccion == "4":
        return auto4
    else:
        print("Selección inválida.")
        return None

def seleccionar_interior():
    print("Seleccione el interior:")
    print("1) Alcántara, Negro con rojo")
    print("2) Piel, Café")
    print("3) Tela, Negro")
    print("4) Alcantar y Cuero, Negro y Blanco")
    seleccion = (input("Ingrese el número del interior: "))
    if seleccion == "1":
        return interior1
    elif seleccion == "2":
        return interior2
    elif seleccion == "3":
        return interior3
    elif seleccion == "4":
        return interior4
    else:
        print("Selección inválida.")
        return None

while True:
    menu()
    opcion = (input("Seleccione una opción: "))
    
    if opcion == "1":
        auto = seleccionar_auto()
        if auto:
            dueño.comprar_auto(auto)
    
    elif opcion == "2":
        auto = seleccionar_auto()
        if auto:
            interior = seleccionar_interior()
            if interior:
                auto.elegir_interior(interior)
    
    elif opcion == "3":
        auto = seleccionar_auto()
        if auto:
            auto.encender()
    
    elif opcion == "4":
        auto = seleccionar_auto()
        if auto:
            dueño.manejar_auto(auto)
    
    elif opcion == "5":
        auto = seleccionar_auto()
        if auto:
            mecanico.reparar_auto(auto)
    
    elif opcion == "6":
        mecanico.autos_reparados()
    
    elif opcion == "7":
        auto = seleccionar_auto()
        if auto1:
            auto1.agregar_motor(motor1)
            auto.descripcion()
        elif auto2:
            auto2.agregar_motor(motor2)
            auto.descripcion()
        elif auto3:
            auto3.agregar_motor(motor3)
            auto.descripcion()
        elif auto4:
            auto4.agregar_motor(motor4)
            auto.descripcion()    
        else:
            print("Selección inválida.")
    
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Intente nuevamente.")