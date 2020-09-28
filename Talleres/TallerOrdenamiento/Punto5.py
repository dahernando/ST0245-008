import time
inicio = time.time()
def ganador(lista):
    aux = 0;
    candidato=0;
    gano = True
    for i in range(0,len(lista)-1):
        max =0
        for j in range(i,len(lista)):
            if(lista[i] == lista[j]):
                max = max +1;
        if max>aux:
            aux = max
            candidato =lista[i]
        elif max ==aux and i == lista[len(lista)-1]:
            print("Hubo un empate")
            gano =False
            break
        else:
            continue
    if(gano):
        print("gano el candidato",candidato, "con",aux,"votos")

ganador([1,1,1,1,1,1,2,3,3,3,3,3,3,3,4,5,6,6,6,6,6])
print("La complejidad del arlgoritmo es de: o(n²) ")
print("El tiempo total de ejecucion fue de:", time.time()-inicio)
