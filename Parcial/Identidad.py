def recursion(n):
    if n==0:
        return n
    else:
        print(n, end=" ")
        recursion(n-1)
        
n = int(input("Ultimos dos digitos de la tarjeta de identidad "))
recursion(n)