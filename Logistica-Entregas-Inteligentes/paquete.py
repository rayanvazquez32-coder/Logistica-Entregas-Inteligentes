class Paquete:
    def __init__(self, codigo, peso, destino, cliente):
        self.codigo = codigo
        self.peso = peso
        self.destino = destino
        self.estado = "Pendiente"
        self.cliente = cliente

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def __str__(self):
        return f"Código: {self.codigo} | Peso: {self.peso} kg | Destino: {self.destino} | Estado: {self.estado}"