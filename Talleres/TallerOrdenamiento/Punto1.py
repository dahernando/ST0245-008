import time

inicio = time.time()
lista =[4,7,11,4,9,5,11,7,3,5]
def order(lista):
    lista1=[]
    for i in lista:
        if i not in lista1:
            lista1.append(i) 
    return lista1
print(order(lista)) 
print("La complejidad del algoritmo es: o(n²)")
print("El tiempo de ejecucion total fue de:",time.time()-inicio)

##################################################
'''#Punto 6 parte c(Implementacion)
#Igualo la lista nuevamente para que no este en orden
lista =[4,7,11,4,9,5,11,7,3,5]
#Implementacion del metodo sort del punto 6
lista.sort()
print(lista)'''
