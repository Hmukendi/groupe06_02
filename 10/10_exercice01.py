# Ce programme demande un mot d'au moins 5 lettres extrait et affiche la partie centrale (sans les 2 premières et 2 dernières lettres).

# 1.Entrées
mot = input("Entrez un mot (min. 5 lettres) :")

# 2.Affichage
if len(mot) >= 5:
    milieu = mot[2:-2]
    print(f"Partie centrale {milieu}")
else:
    print("Mot trop court.")
