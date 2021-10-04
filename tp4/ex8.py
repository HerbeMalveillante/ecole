def addition(liste, liste2):
    
    liste = "".join([str(i) for i in liste])
    liste2 = "".join([str(i) for i in liste2])

    max_len = max(len(liste),len(liste2))
    liste = liste.zfill(max_len) # on rajoute des zéros devant
    liste2 = liste2.zfill(max_len) # on rajoute des zéros devant

    result = ""

    carry = 0



    for i in range(max_len-1, -1, -1):

        r = carry # somme temporaire de l'addition
        r += 1 if liste[i] == '1' else 0 # on ajoute la somme
        r += 1 if liste2[i] == '1' else 0 # on ajoute la somme
        result = ('1' if r % 2 == 1 else '0') + result # on calcule la valeur du bit
  
        # On calcule la retenue
        carry = 0 if r < 2 else 1

    if carry != 0: # on rajoute la retenue si il en reste une à la fin
        result = '1' + result
    
    return [int(i) for i in result]

print(addition([1101],[100]))