def sommeDeCubes():
    output = []
    for i in range(100, 1000):
        a, b, c = str(i)

        if i == int(a)**3 + int(b)**3 + int(c)**3:
            output.append(i)
    return output

def sommeDePuissances(n):

    output = []
    for i in range(100, n+1):
        numberList = [j for j in str(i)]
        if sum([int(n)**len(numberList) for n in numberList]) == i:
            output.append(i)
    return output

print(sommeDePuissances(10000))