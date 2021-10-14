def multiples(a, b, n):
    total = []
    for i in range(1, n + 1):
        if i % a == 0 or i % b == 0:
            total.append(i)
    return total


print(multiples(7, 3, 30))
