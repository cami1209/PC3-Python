class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.num_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
        else:
            print("Notas: No asignadas")

    def set_age(self, edad):
        self.edad = edad

    def set_nota(self, nota):
        self.notas.append(nota)

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del alumno: ")
    num_registro = input("Ingrese el número de registro del alumno: ")
    alumno = Alumno(nombre, num_registro)

    alumno.set_age(int(input("Ingrese la edad del alumno: ")))
    
    num_notas = int(input("¿Cuántas notas desea ingresar para el alumno?: "))
    for i in range(num_notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        alumno.set_nota(nota)

    alumno.display()
