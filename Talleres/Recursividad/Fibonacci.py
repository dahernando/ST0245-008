def fibo(i):
    if i<=2:
        return i
    else:
        return fibo(i-1)+fibo(i-2)
print(fibo(int(input("Ingrese un numero "))))