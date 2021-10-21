def adresse(prenom, nom):
    return(f"{prenom.lower()}.{nom.lower()}@etu.univ-tours.fr")

print(adresse("Marc", "Barthet"))
print(adresse("marc", "barthet"))

def prenom_nom(s):
    try :
        totalNom = s.split("@")[0]
        prenom, nom = totalNom.split(".")
        return prenom.capitalize(), nom.capitalize()
    except ValueError:
        return None

print(prenom_nom("pacome.renimel@etu.univ-tours.fr"))
print(prenom_nom("adpazod"))