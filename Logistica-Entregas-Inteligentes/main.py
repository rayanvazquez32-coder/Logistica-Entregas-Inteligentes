import csv

def guardar_clientes(lista_clientes):
    with open("clientes.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["id", "nombre", "direccion"])

        for c in lista_clientes:
            escritor.writerow([c.id, c.nombre, c.direccion])