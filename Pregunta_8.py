import random

def generar_numeros():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista generada:", lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

