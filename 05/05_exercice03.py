# Ce programme demande une chaîne à l’utilisateur et construit une nouvelle chaîne inversée à l’aide d’une boucle for.

# 1.Entrées
texte = input("Entrez une chaîne : ")
inverse = ""

# 2.Conditions
for char in texte:
    inverse = char + inverse  # On ajoute chaque caractère devant

# 3.Affichage
print(f"chaîne inversée : {inverse} ")
