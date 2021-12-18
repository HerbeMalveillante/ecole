from math import log, log10


def test_pH():
    while True:
        entree = float(input("Rentrez une concentration molaire : "))
        if 10 ** (-14) < entree < 10 ** (-1):
            break

    pH = round(-log10(entree), 2)

    print(f"La solution a un pH de {pH}")

    if pH >= 7.5:
        print("La solution est basique")
    elif pH <= 6.5:
        print("La solution est acide")
    else:
        print("La solution est à peu près neutre")


test_pH()
