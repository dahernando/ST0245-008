import numpy as np
def Buscar(matriz,elemento):
    for i in np.nditer(matriz, order='F'):
        if i==elemento:
            return True
        else:
            continue
    return False
matriz = np.random.randint(0,100,(6,4))
print("Matriz Generada:\n",matriz)
n= int(input("Ingrese el numero a buscar:\n"))
print(Buscar(matriz,n))


