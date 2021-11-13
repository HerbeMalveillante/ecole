def ecrire(nom, n):
    """creates a file named 'nom', where each lines contains
    'Texte de la ligne n°k', k being between 1 and n."""
    with open(nom, 'w') as f:
        for k in range(1, n+1):
            f.write('Texte de la ligne n°{}\n'.format(k))

def copierEntre(source, destination, n, m):
    """copies the lines n to m from the file 'source' to the file 'destination'."""
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        for k in range(n, m+1):
            f2.write(f1.readline())

def copierLignesPaires(source, destination):
    """copies the line of even index from the file 'source' to the file 'destination'"""
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        for k in range(0, len(f1.readlines()), 2):
            f2.write(f1.readline())

def copierLignesImpaires(source, destination):
    """copies the line of odd index from the file 'source' to the file 'destination'"""
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        for k in range(1, len(f1.readlines()), 2):
            f2.write(f1.readline())