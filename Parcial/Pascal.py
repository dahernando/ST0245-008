n = int(input("Ingrese un numero "))
def  pascal(row, column):
            if row < 0 and column < 0:
                return 0
            elif row == 0 and column == 0:
                return 1
            elif column==row or column==1:
                return 1 
            else:
                return pascal(row-1,column-1)+pascal(row-1,column)      
for i in range(1,n+2):
    for j in range(1,i+1):
        print(pascal(i,j), end=" ")
    print("")  

