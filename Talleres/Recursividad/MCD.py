n = int(input("Primer numero ")) 
m = int(input("Segundo numero ")) 
def MCD(n,m):
    if n<m:
        aux = n
        n=m
        m=aux
    if n%m==0:
        return m
    else:
        return MCD(m,n%m)
print(MCD(n,m))