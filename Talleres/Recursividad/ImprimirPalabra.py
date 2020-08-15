def imprimirL(palabra,m):
    if m==0:
        return print(palabra)
    else:
        return print(palabra[:(len(palabra)-m)]),imprimirL(palabra,m-1)

palabra = "Bienvenidos"
imprimirL(palabra,len(palabra)-1)
