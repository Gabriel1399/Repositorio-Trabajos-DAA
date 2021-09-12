from array import array

arr = array("i", [88, 67, 44, 35, 30, 10])
limOrdenados = 0

for numPasada in range(0, len(arr)-1):
    indComparacion = limOrdenados + 1

    while indComparacion > 0 and arr[indComparacion] < arr[indComparacion -1]:
        aux = arr[indComparacion]
        arr[indComparacion] = arr[indComparacion-1]
        arr[indComparacion-1] = aux
        indComparacion -= 1

    limOrdenados+=1

for i in arr:
    print(i)