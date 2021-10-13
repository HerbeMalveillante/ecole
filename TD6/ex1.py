from time import time

def division_euclidienne_dichotomique(a, b):
    """Renvoie le quotient q et le reste r de la division euclidienne de a par b"""

    n = 0
    while 2**n * b <= a:
        n += 1
    inf = 2**(n-1)
    sup = 2**n 
    for i in range(1, n):
        mid = (inf + sup)/2
        if mid * b <= a:
            inf = mid
        else :
            sup = mid
    return inf, a-b*inf

print(division_euclidienne_dichotomique(153,28))

def division_euclidienne_decimale(a, b):
    """renvoie le quotient et le reste de la division euclidiennede a par b"""
    q = 0
    while a > b:
        n = 0
        while 10**n * b <= a:
            n += 1
        n -= 1
        c = 0
        while c*10**n*b <= a:
            c += 1
        c -= 1
        q = q+c*10**n
        a = a-c*10**n*b
    return q, a

print(division_euclidienne_dichotomique(153,28))



# EXERCICE 2

print(division_euclidienne_dichotomique(1630,8))

def divis_euclid(dividende, diviseur):
    quotient = 0
    while dividende >= diviseur:
        dividende -= diviseur
        quotient += 10
    return quotient, dividende