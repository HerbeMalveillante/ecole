import random

print("\n"*20)
print("-"*20)

def allumettes(nombreAllumettes):
    restantes = nombreAllumettes
    bot = random.choice([True, False])

    print(f"Le hasard a décidé de faire commencer le {'bot' if bot else 'joueur'}.")

    while restantes > 1:
        restantes -= tour(restantes, bot)
        bot = False if bot else True
    
    if restantes > 0:
        print(f"Il ne reste qu'une seule allumette ! Le {'joueur' if bot else 'bot'} a gagné !")
    else : 
        print(f"Le {'joueur' if bot else 'bot'} a pris la dernière allumette : Il a perdu !")
    

def tour(nombreAllumettes, bot):

    print(f"{nombreAllumettes*'|'} ({nombreAllumettes}) -> C'est au {'bot' if bot else 'joueur'} de jouer !")

    if bot :
        # on génère les multiples de 4 + 1 et on récupère le dernier avant le nombre d'allumettes, forcément accessible en prenant
        # une à trois allumettes.
        positionGagnante = [i for i in range(1, nombreAllumettes, 4)][-1]

        # dans le cas où le joueur joue en premier et arrive à mettre le nombre d'allumettes à un multiple de 4+1,
        # notre bot va vouloir prendre 4 allumette pour récupérer un multiple de 4+1. C'est interdit, on prends donc
        # trois allumettes mais si le joueur connaît l'astuce et ne fait plus d'erreur, le bot a forcément perdu.

        choix = nombreAllumettes - positionGagnante
        if choix > 3 :
            choix = 3

        print(f"Le bot a chosi de retirer {choix} allumettes.")
        return choix

        # pour un bot qui fait ses choix au pif :
        # choix = random.choice(range(1, min(nombreAllumettes, 3)+1))
        # print(f"Le bot a choisi de retirer {choix} allumettes.")
        # return choix
    else :
        choix = None
        choixPossibles = range(1, min(nombreAllumettes, 3)+1)
        while choix not in choixPossibles:
            choix = int(input(f"Combien d'allumettes souhaitez vous retirer ? (choix possibles : <{', '.join([str(choix) for choix in choixPossibles])}>): "))
        print(f"Le joueur a choisi de retirer {choix} allumettes.")
        return choix


allumettes(random.randint(10, 20))