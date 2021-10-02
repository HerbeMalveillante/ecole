def factoriel(n):
    total = 1
    for i in range(n):total=total*(i+1)
    return total

def binome(n, p):
    return int(factoriel(n)/(factoriel(p)*factoriel(n-p)))

def main():
    n = int(input("Entrez une valeur de n : "))
    p = -1
    while p not in range(0, n+1):
        p = int(input("Entrez une valeur de p comprise entre 0 et n : "))
    
    print(binome(n, p))

def binomeNewton(n):

    output = []
    for i in range(n+1):

        strOut = ""
        if binome(n, i) != 1:
            strOut += str(binome(n, i))
            strOut += " "
        if n-i != 0:
            strOut += f"a^{n-i} "
        if i != 0 :
            strOut += f"b^{i} "
        output.append(strOut)
    
    print("+ ".join(output))

def main2():
    n = int(input("Entrez une valeur de n : "))
    binomeNewton(n)

def trianglePascal(n):
    triangle = []

    for i in range(n):

        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else : 
            ligne = []
            for j in range(i+1):
                if j == 0 or j == i:
                    ligne.append(1)
                else :
                    ligne.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(ligne)
        

    print("\n".join([" ".join([str(el) for el in ligne]) for ligne in triangle]))