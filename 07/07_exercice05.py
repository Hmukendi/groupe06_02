# Ce programme demande une liste et la renverse

# 1.Entrées
entree = input("Entrez des éléments :")
liste = entree.split()

# 2.Inversion
liste_inversee = []
for i in range(len(liste) - 1, -1, -1):
    liste_inversee.append(liste[i])

# 3.Affichage
print(f"Liste inversée : {liste_inversee}")
