f = open('p022_names.txt', 'r')
f.split(",")
F=sorted(f)

def correspondance(f):
    ### Permet de renvoyer un numero correspodant au rang dans l'alphabet d'une lettre donnée en entrée ###
    L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    k=0
    while f!=L[k]:
        k=k+1
    return k+1

def euler22(f):
    s=0
    for k in range(len(f)):
        for i in range(len(f[k])):
            s+=correspondance(f[k][i])*(k+1)
    return s        
    
print (euler22(F))
### Resultat: 871198282 ###
### Il m'était impossible d'ouvrir le fichier .txt dans python, je l'ai donc fait à la main en faisant un copié collé ###