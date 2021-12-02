def resultat(s):
    """the s argument is a string in the form 'name : result',
    where the result is a float or an int representing a note between 0 and 20 or the text 'DEFAILLANT' that can be capitalized arbitrarily.
    return the results. Returns False if the result is not a number."""
    result = s.split(":")
    if (
        result[1].strip().upper() == "DEFAILLANT"
        or result[1].strip().upper() == "DÉFAILLANT"
    ):
        return False
    else:
        return float(result[1].strip())


def repartir(source, admis, ajournes, defaillants):
    """opens the source file that contains lines in the form 'name : result'.
    Skips empty lines.
    For each line/student, if the result is greater than 10, stores the corresponding line in the 'admis' files.
    If the result is smaller than 10, stores the corresponding line in the 'ajournes' file. If the result is not a number,
    store the corresponding line in the 'defaillants' file.

    Example of function call : 'repartir("notes.txt", "admis.txt", "ajournes.txt", "defaillants.txt")'"""
    with open(source, "r") as f:
        for line in f:
            if line.strip() != "":
                if resultat(line) == False:
                    with open(defaillants, "a") as f:
                        f.write(line)
                elif resultat(line) > 10:
                    with open(admis, "a") as f:
                        f.write(line)
                elif resultat(line) < 10:
                    with open(ajournes, "a") as f:
                        f.write(line)


repartir("notes.txt", "admis.txt", "ajournes.txt", "defaillants.txt")
