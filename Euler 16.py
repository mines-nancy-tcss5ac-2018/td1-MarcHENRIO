def solve(n) :
    nombre= 2**n
    n = str(nombre)
    s = 0
    for k in range (len(n)):
        s += int(n[k])
    return s

print (solve(1000)) 