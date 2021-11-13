def copier(source, destination):
    f=open(source, 'r')
    g=open(destination, 'w')
    for texte in f:
        g.write(texte)
    f.close()
    g.close()

def numeroter(source, destination):
    """copies the source file into the destination file line per line, putting each line in the destination file between a pair of brackets []"""
    f=open(source, 'r')
    g=open(destination, 'w')
    for texte in f:
        g.write("["+texte+"]")
    f.close()
    g.close()