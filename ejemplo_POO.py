# Ejemplo capítulo 2.1.3 POO

class Vehiculo(object):
    def __init__(self, tipo, marca, color):
        self.tipo = tipo
        self.marca = marca
        self.color = color

    def acelerar(self):
        print(f"El {self.tipo} está acelerando")

    def frenar(self):
        print(f"El {self.tipo} está frenando")

class Coche(Vehiculo):
    def __init__(self, tipo, marca, color, num_puertas):
        super().__init__(tipo, marca, color)
        self.num_puertas = num_puertas

    def abrir_puerta(self):
        print(f"El {self.tipo} está abriendo la puerta")

class Avion(Vehiculo):
    def __init__(self, tipo, marca, color, num_asientos):
        super().__init__(tipo, marca, color)
        self.num_asientos = num_asientos

    def despegue(self):
        print(f"El {self.tipo} está despegando")

if __name__ == '__main__':
    # Instanciamos los vehículos
    v = Vehiculo('Coche', 'Audi', 'Negro')
    c = Coche('Coche', 'Mercedes', 'Azul', '5')
    a = Avion('Avion', 'Boeing', 'Blanco', '235')

    # Acciones
    v.acelerar()

    c.acelerar()
    c.frenar()
    c.abrir_puerta()

    a.acelerar()
    a.despegue()


