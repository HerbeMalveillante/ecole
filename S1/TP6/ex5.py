def comptage(s, suite):
    return len([i for i in s if i in suite])


print(comptage("Hervé et Irène se sont même rencontrés à Noël", "eéèëê"))
