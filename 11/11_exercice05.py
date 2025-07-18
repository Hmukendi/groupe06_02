# Ce programme génère un mot de passe aléatoire de longueur donnée, composé de lettres et chiffres.
import random
import string

# 1.Définition de la foncion
def generer_mdp (longueur):
    caracteres = string.ascii_letters + string.digits
    mdp = '' .join(random.choice(caracteres) for _ in range (longueur))
    return mdp

# 2.Entrées
longueur= int (input ("Longueur du mot de passe: "))

# 3.Affichage
print (f"Mot de passe généré: {generer_mdp(longueur)} ")
