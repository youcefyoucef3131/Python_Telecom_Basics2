def  signe_z(x):
    if x==0:
        print(x,'est nul')
    elif x<0:
        print(x,'est négatif')
    else :
        print(x,'est positif')
        
    return x
valeur=int(input("entrer votre nombre"))
signe_z(valeur)