import numpy as np
import time
inicio = time.time()
v = np.array([1,1,1,1,2,2,2,3,3,4,4,5,5,5])
def ordenar(vector):
    lista = []
    for i in v:
        if len(lista)== 0:
            lista.append(i)
        elif i != lista[len(lista)-1]:
            lista.append(i)
    resultado = np.array(lista) 
    return resultado
print(ordenar(v))
print("La complejidad del algoritmo es: o(n)")
print("El tiempo de ejecucion total fue de:",time.time()-inicio)


##################################################
'''#Punto 6 parte c(Implementacion)
#Igualo la lista nuevamente para que no este en orden
v=np.array([1,1,1,1,2,2,2,3,3,4,4,5,5,5])
#Implementacion del metodo sort del punto 6
v.sort()
print(v)'''
