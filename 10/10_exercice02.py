# Ce programme demande une liste d’éléments et affiche la liste inversée avec slicing

# 1.Entrées
entree = input("Entrez des éléments séparés par des espaces :")

# 2.Inversion
liste = entree.split()
liste_inversee = liste[::-1]

# 3.Affichage
print(f"Liste inversée {liste_inversee}")
