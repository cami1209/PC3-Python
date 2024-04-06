def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en el formato X/Y: ")
            x, y = map(int, fraccion.split('/'))
            if x <= 0 or y <= 0:
                raise ValueError("Los números deben ser positivos")
            if x > y:
                raise ValueError("El numerador debe ser menor o igual al denominador")
            return x, y
        except ValueError as ve:
            print(f"Error: {ve}. Intente nuevamente.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser cero. Intente nuevamente.")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100
    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return round(porcentaje)

def main():
    while True:
        try:
            x, y = obtener_fraccion()
            porcentaje = calcular_porcentaje(x, y)
            if porcentaje == 'E':
                print("Cantidad de combustible en el tanque: E")
            elif porcentaje == 'F':
                print("Cantidad de combustible en el tanque: F")
            else:
                print(f"Cantidad de combustible en el tanque: {porcentaje}%")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
