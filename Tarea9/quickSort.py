def quickSort(datos, izq, der):
    if izq < der:
        indiceParticion = particion(datos, izq, der)
        quickSort(datos, izq, indiceParticion)
        quickSort(datos, indiceParticion + 1, der)


def particion(datos, izq, der):
    pivote = datos[izq]
    while True:
        while datos[izq] < pivote:
            izq += 1

        while datos[der] > pivote:
            der -= 1

        if izq >= der:
            return der
        else:
            datos[izq], datos[der] = datos[der], datos[izq]
            izq += 1
            der -= 1

info = [50, 96, 1, 6, 80, 654, 10, 96, 684, 848, 541, 706, 354, 165, 87, 354, 87, 56, 98, 13, 46, 25, 12, 87]
print("Arreglo recibido: ")
print(info)
quickSort(info, 0, len(info) - 1)
print("Arreglo ordenado: ")
print(info)