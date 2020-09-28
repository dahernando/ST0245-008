import random
def generarLista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0,100))
    return lista
def quickSort(lista):
    izquierda= []
    derecha = []
    centro = [] 

    if len(lista)>1:
        pivote = lista[len(lista)-1]
        for i in lista:
            if(i<pivote):
                izquierda.append(i)
            elif(i==pivote):
                centro.append(i)
            else:
                derecha.append(i)
        return quickSort(izquierda)+centro+ quickSort(derecha)
    else:
        return lista
A = generarLista(60)
B = generarLista(100)
print("Lista A:\n",A)
print("##############################################################################################################################")
print("Lista B:\n",B)
print("##############################################################################################################################")
print("Lista A ordenada:\n",quickSort(A))
print("##############################################################################################################################")
print("Lista B ordenada:\n",quickSort(B))
print("##############################################################################################################################")
C =[]
C.extend(A)
C.extend(B)
print("Lista C: listas A y B iniciales unidas:\n",C)
print("##############################################################################################################################")
print("Lista C ordenada:\n",quickSort(C))

