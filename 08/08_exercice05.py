# Ce programme demande un texte et affiche uniquement les consonnes.

# 1.Entrées
texte = input("Entrez un texte :")

# 2.Affichage
voyelles = "aeiouyAEIOUY"
for char in texte:
    if char.isalpha() and char not in voyelles:
        print(char, end="")
