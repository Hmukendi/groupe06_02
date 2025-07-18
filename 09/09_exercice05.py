# Ce programme demande une phrase et un mot puis remplace ce mot par des astérisques

# 1.Entrées
phrase = input("Entrez une phrase :")
mot = input("Mot à masquer : ")

# 2.Masquage
masque = "*" * len(mot)
nouvelle_phrase = phrase.replace(mot, masque)

# 3.Affichage
print(f"Phrase après masquage {nouvelle_phrase}")
