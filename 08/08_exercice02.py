# Ce programme demande une liste d’éléments et affiche chaque élément avec son indice

# 1.Entrées
entree = input("Entrez des éléments :")
liste = entree.split()

# 2.Affichage
for i, elem in enumerate(liste):
    print(f"Indice {i} : {elem}")
