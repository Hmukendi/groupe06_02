# Ce programme crée une "matrice" 3×3 (liste de listes) et affiche chaque ligne et chaque élément.

# 1.Entrées
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2.Affichage
for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
    print()
