class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Ejemplo de uso
if __name__ == "__main__":
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    mi_rectangulo = Rectangulo(largo, ancho)
    area = mi_rectangulo.calcular_area()
    print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")
