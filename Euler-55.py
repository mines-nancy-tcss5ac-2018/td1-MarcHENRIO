def nombre_renversé(n) :
    a = str(n)
    return int(a[::-1])

def est_un_nombre_de_Lychrel (n) :
    for i in range(50) :
        s = n + nombre_renversé(n)
        if str(s) == str(nombre_renversé(s)) :
            return False
    else :
        return True

assert est_un_nombre_de_Lychrel (196) == True

def solve(n) :
    c = 0
    for k in range (n+1) :
        if est_un_nombre_de_Lychrel (k) :
            c += 1
    return c

print (solve(10000))
        