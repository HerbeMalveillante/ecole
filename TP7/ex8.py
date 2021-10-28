import random

presentateur = {(1, 1): (2, 3), (1, 2): (3, 3), (1, 3): (2, 2), (2, 1): (3, 3), (2, 2): (1, 3), (2, 3): (1, 1), (3, 1): (2, 2), (3, 2): (1, 1), (3, 3): (1, 2)}
alea = {1:(2,3), 2:(1,3), 3:(1,2)}
change = {(1,2):3, (1,3):2, (2,1):3, (2,3):1, (3,1):2, (3,2):1}

def choix_presentateur(porte_gagnante, porte_joueur_debut):
    return random.choice(presentateur[(porte_gagnante, porte_joueur_debut)])

def strategie_alea(porte_debut, porte_ouverte):
    return random.choice([change[(porte_debut, porte_ouverte)], porte_debut])

def strategie_change(porte_debut, porte_ouverte):
    return change[(porte_debut, porte_ouverte)]

def strategie_garde(porte_debut, porte_ouverte):
    return porte_debut

def experience(n):

    stats = {"alea":0, "change":0, "garde":0}

    for i in range(n):
        porte_gagnante = random.choice([1,2,3])
        porte_joueur_debut = random.choice([1,2,3])
        porte_ouverte = choix_presentateur(porte_gagnante, porte_joueur_debut)

        if porte_gagnante == strategie_alea(porte_joueur_debut, porte_ouverte):
            stats["alea"] += 1
        if porte_gagnante == strategie_change(porte_joueur_debut, porte_ouverte):
            stats["change"] += 1
        if porte_gagnante == strategie_garde(porte_joueur_debut, porte_ouverte):
            stats["garde"] += 1
    
    print(f"La stratégie aléatoire a {round((stats['alea']/n) * 100,2)}% de chances de fonctionner.")
    print(f"La stratégie change a {round((stats['change']/n) * 100,2)}% de chances de fonctionner.")
    print(f"La stratégie garde a {round((stats['garde']/n) * 100,2)}% de chances de fonctionner.")
    return stats

print(experience(1000))