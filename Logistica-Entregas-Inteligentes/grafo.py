class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_zona(self, zona):
        if zona not in self.grafo:
            self.grafo[zona] = []

    def conectar(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def buscar_ruta(self, origen, destino, visitados=None):
        if visitados is None:
            visitados = []

        visitados.append(origen)

        if origen == destino:
            return visitados

        for vecino in self.grafo[origen]:
            if vecino not in visitados:
                ruta = self.buscar_ruta(vecino, destino, visitados.copy())
                if ruta:
                    return ruta

        return None