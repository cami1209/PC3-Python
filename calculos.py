import operaciones

if __name__ == "__main__":
    # Ejemplos de uso de las funciones
    print("Suma:", operaciones.suma(5, 3))
    print("Resta:", operaciones.resta(10, 7))
    print("Producto:", operaciones.producto(4, 6))
    print("División:", operaciones.division(8, 2))
    print("Intentando dividir por cero:")
    operaciones.division(10, 0)
    print("Intentando sumar un número con una cadena:")
    operaciones.suma(5, "cadena")
