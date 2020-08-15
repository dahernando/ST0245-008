b = int(input("Ingrese base "))
e = int(input("Ingrese la exponente "))
def Potencia(b,e):
    if e==0:
        return 1
    else:
        return b*Potencia(b,e-1)
print(Potencia(b,e))