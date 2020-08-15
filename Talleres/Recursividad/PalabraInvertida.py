def Invertir(palabra):
    if len(palabra)==1:
        return palabra
    else:
        return palabra[len(palabra)-1]+Invertir(palabra[:-1])

palabra = input("Ingrese una palabra")
print(Invertir(palabra))