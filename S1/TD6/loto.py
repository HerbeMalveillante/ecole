def uncentime(jours):

    total = [0.01]

    for i in range(jours - 1):
        total.append(total[-1] * 2)

    return sum(total)


print(uncentime(30))
