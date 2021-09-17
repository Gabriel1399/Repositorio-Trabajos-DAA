from itertools import product  

def permutacionRepeticion(lista, m):
    for i in product(lista, repeat = m): #producto cartesiano
        print(i)    

lista = [1, 2, 3]
n = len(lista)
m = 3

permutacionRepeticion(lista, m)
NumPerRep = pow(n, m) #Numero de permutaciones con repetcio

print("Final:",NumPerRep)