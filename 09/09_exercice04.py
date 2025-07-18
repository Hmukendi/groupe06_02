# Ce programme demande un titre ou une phrase, génére un acronyme en prenant la première lettre de chaque mot en majuscule.

# 1.Entrées
phrase = input("Entrez une phrase ou un titre :")

# 2.création
mots = phrase.split()
acronyme = ""
for mot in mots:
    acronyme += mot[0].upper()

# 3.Affichage
print(f"Acronyme: {acronyme}")
