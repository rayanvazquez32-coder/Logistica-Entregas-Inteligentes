class Repartidor:
    def __init__(self, nombre, vehiculo, zona_actual):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.zona_actual = zona_actual
        self.paquetes_asignados = []

    def asignar_paquete(self, codigo_paquete):
        self.paquetes_asignados.append(codigo_paquete)

    def __str__(self):
        return f"Repartidor: {self.nombre} | Vehículo: {self.vehiculo} | Zona: {self.zona_actual}"