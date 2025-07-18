# Ce programme demande un texte, retire tous les espaces en trop (avant et après), convertit en minuscules et remplace tous les points par des points d’exclamation.

# 1.Entrées
texte = input("Entrez un texte :")

# 2.nettoyage
texte = texte.strip().lower().replace(".", "!")

# 3.Affichage
print(f"Texte nettoyé : {texte}")
