
class Cliente:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.historial_pedidos = []

    def agregar_pedido(self, codigo_paquete):
        self.historial_pedidos.append(codigo_paquete)

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Dirección: {self.direccion}"