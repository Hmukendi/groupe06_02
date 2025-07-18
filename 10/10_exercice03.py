# Ce programme demande une phrase et crée une liste contenant un mot sur deux.

# 1.Entrées
phrase = input("Entrez une phrase :")

# 2.Extraction
mots = phrase.split()
un_sur_deux = mots[::2]

# 3.Affichage
print(f"Mots un sur deux {un_sur_deux}")
