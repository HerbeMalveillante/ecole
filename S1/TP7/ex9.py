def calculMinimum():

    a_min = 1
    b_min = 2
    c_min = 3
    d_min = 4

    resultat_min = (10 * a_min + b_min - c_min) * d_min

    a = 1

    while a <= 4:
        b = 1
        while b <= 4:
            c = 1
            while c <= 4:
                d = 1
                while d <= 4:
                    if list(set([a, b, c, d])) == [
                        a,
                        b,
                        c,
                        d,
                    ]:  # si ils sont tous différents
                        print("TOP")
                        resultat = (10 * a + b - c) * d
                        print(resultat)
                        if resultat < resultat_min:
                            resultat_min = resultat
                            a_min = a
                            b_min = b
                            c_min = c
                            d_min = d

                            print(
                                "(",
                                a_min,
                                b_min,
                                "-",
                                c_min,
                                ") *",
                                d_min,
                                "=",
                                resultat_min,
                            )

                    d += 1
                c += 1
            b += 1
        a += 1
    return (a_min, b_min, c_min, d_min, resultat_min)


print(calculMinimum())


def permutations(start, end=[]):
    if len(start) == 0:
        print(end)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i + 1 :], end + start[i : i + 1])


permutations([4, 5, 6])
