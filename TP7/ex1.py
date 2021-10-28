def f(n):
    if 0<=n and n<=7:
        return n-1
    else :
        return f(n+3)

# print(f(8))
# on constate que les conditions d'arrêt ne fonctionnent pas comme prévu :
# si on entre une valeur de n supérieure à 7, la récursion ne prend jamais fin.

def g(n):
    if (n>=6):
        return n-1
    else :
        return g(n-8)

# idem mais dans l'autre sens.

def h(n):
    if (n<=10):
       return 3
    else:
       return h(n-8)

# cette fonction fonctionne comme prévu

print(h(100))
print(h(-100))