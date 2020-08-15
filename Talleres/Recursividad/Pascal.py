n = int(input("Ingrese un numero "))
def pascal(fila,colum):
    if(colum==1 or colum==fila):
        return 1
    else:
        return pascal(fila-1,colum-1)+pascal(fila-1,colum)

for i in range(1,n+2):
    for j in range(1,i+1):
        print(pascal(i,j), end=" ")
    print("")  

