i = int(input("Ingrese un numero"))
def tor(n):
    if n==0:
        return 1
    elif n==i:
        x=(2*tor(n-1))-1
        return x
    else:
        return 2*tor(n-1)
print(tor(i))