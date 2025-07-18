# Ce programme demande une liste à l’utilisateur et la filtre.

# 1.Entrées
entree = input("Entrez des valeurs (séparées par des espaces) :")

# 2.Filtrage
liste = entree.split()
uniques = []
for item in liste:
    if item not in uniques:
        uniques.append(item)

# 3.Affichage
print(f"Liste sans doublons {uniques}")
