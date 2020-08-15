def Palindrom(palabra):
        if len(palabra)<=1:
            return "Es palindromo"
        elif palabra[len(palabra)-1] == palabra[0]:
            return Palindrom(palabra[1:len(palabra)-1])
        else:
            return "No es palindromo"

print(Palindrom("ANA"))