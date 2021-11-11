def string_match_brute(A, P):
    contador = 0
    for i in range((len(A)-len(P))+1):
        for j in range(len(P)):
            if P[j] == A[i+j]:
                pass
            else:
                break
        if j+1 == len(P) and A[i+j] == P[j]:
            print(f"Se encontro {P} en la posicion: {i}")
            contador+=1
    print(f"El patron {P} se encontro {contador} veces\n")

def impresion(A, P1, P2, P3):
    string_match_brute(A, P1)
    string_match_brute(A, P2)
    string_match_brute(A, P3)

f = open("el_quijote_ii.txt", "r", encoding="utf8")
entrada = f.read()
patron1 = "hidalgo"
patron2 = "molino"
patron3 = "merced"
impresion(entrada, patron1, patron2, patron3)
f.close()
