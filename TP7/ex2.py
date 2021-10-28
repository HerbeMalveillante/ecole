def binome(n, p):
    if p == 0 or p == n :
        return 1
    
    return binome(n-1, p-1) + binome(n-1, p)

print(binome(8,5))