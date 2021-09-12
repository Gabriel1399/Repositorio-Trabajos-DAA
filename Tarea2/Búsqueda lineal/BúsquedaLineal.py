from array import array

arr = array("i", [10, 30, 35, 44, 67, 88])
numeroBuscar = 30
exito = False
indice = 0
posicion = 0
while (not exito) and indice < len(arr):
    if  numeroBuscar == arr[indice]:
        exito = True
        posicion = indice
    indice+=1

if exito:
    print("El dato a buscar se encuentra en la posicion", posicion, "del arreglo")
else:
    print("El dato a buscar no se encuentra en el arreglo")