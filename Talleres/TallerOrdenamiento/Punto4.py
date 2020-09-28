def VariableIntercambios():
    global intercambios
    intercambios=0

def mostrarVariableGlobal():
    return intercambios

def editarVariable(x):
    global intercambios
    intercambios+=x

def shellSort(lista):
    mitad = len(lista)//2
    i =0
    while mitad >= 1:
      for posicion_inicial in range(mitad):
        reducir_busqueda(lista, posicion_inicial, mitad)

      print("pasada",i+1,"-> nueva lista", lista)
      i =i+ 1
      mitad = mitad//2
    print("Se necesitan",i,"pasadas para ordenar la siguiente lista:")
    print("[8,43,17,6,40,16,18,97,11,7]")
def reducir_busqueda(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):
        x=0
        current_value = nlist[i]
        posicion = i
        while posicion>=gap and nlist[posicion-gap]>current_value:
            nlist[posicion]=nlist[posicion-gap]
            posicion = posicion-gap
            nlist[posicion]=current_value
            x +=1
        editarVariable(x)
    
VariableIntercambios()    
lista= [8,43,17,6,40,16,18,97,11,7]
shellSort(lista)
print("Con un total de intercambios:",mostrarVariableGlobal())
'''#Punto 5 parte c(Implementacion)
#Igualo la lista nuevamente para que no este en orden
lista =[8,43,17,6,40,16,18,97,11,7]
#Implementacion del metodo sort del punto 6
lista.sort()
print(lista)'''
