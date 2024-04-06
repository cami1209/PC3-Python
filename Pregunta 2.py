def obtener_calificaciones():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista = calificaciones_str.split(',')
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Uno o más valores introducidos no son calificaciones válidas. Intente nuevamente.")

def main():
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)

if __name__ == "__main__":
    main()
