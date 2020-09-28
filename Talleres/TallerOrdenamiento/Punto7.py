import time
inicio = time.time()
def EncontrarNegativos(lista):
    listaNegativos = []
    for i in lista:
        if i<0:
            listaNegativos.append(i)
        else:
            continue
    return listaNegativos

lista = [-1,-2,-3,1,2,3]
print(EncontrarNegativos(lista))
print("La complejidad del algoritmo es o(n)")
print("Siempre debe recorrer los n elementos porque puede que el ultimo elemento sea negativo")
print("El tiempo total de ejecucion es:", time.time()-inicio)
