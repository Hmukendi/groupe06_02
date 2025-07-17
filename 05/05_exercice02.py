# Ce programme demande une liste d’entiers à l’utilisateur (saisie séparée par des espaces) et calcule la somme des nombres pairs uniquement.

# 1.Entrées
entree = input("Entrez des nombres séparés par des espaces : ")
liste = [int(x) for x in entree.split()]

# 2.Initialisation
somme_pairs = 0

# 3.Résultat
for nombre in liste:
    if nombre % 2 == 0:
        somme_pairs += nombre

# 4.Affichage
print(f"somme des nombres pairs {somme_pairs}")
