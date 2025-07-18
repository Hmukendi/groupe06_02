# Ce programme demande une liste de nombres, crée une nouvelle liste contenant uniquement les éléments situés aux indices pairs.

# 1.Entrées
entree = input("Entrez des nombres séparés par des espaces :")

# 2.Extraction 
liste = entree.split()
elements_pairs = liste[::2]

# 3.Affichage
print(f"Éléments aux indices pairs {elements_pairs}")
