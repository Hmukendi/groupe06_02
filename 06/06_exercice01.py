# Ce programme est un jeu qui demande à l’utilisateur de deviner le nombre qu'i génère entre 0 et 100

import random

# 1.Génération d'un nombre aléatoire
nombre_secret = random.randint(1, 100)

# 2.Entrées et Affichage
essai = None
while essai != nombre_secret:
    essai = int(input("Devine le nombre (1-100) :"))
    if essai < nombre_secret:
        print("Trop petit.")
    elif essai > nombre_secret:
        print("Trop grand.")
    else:
        print("Bravo, tu as trouvé !")