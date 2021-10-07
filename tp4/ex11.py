from math import log10, floor

def nombreChiffres(entier):
    return int(floor(log10(entier)))+1

def sommeChiffres(entier):
    return sum([int(i) for i in str(entier)])