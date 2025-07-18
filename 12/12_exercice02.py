# Ce programme demande un nombre et crée un fichier contenant sa table de multiplication (1 à 12).

# 1.Entrées
nombre = int(input("Nombre pour la table de multiplication : "))

with open( "table.txt" , "w" , encoding="utf-8" ) as f:
    for i in range(1, 13):
        ligne= f" {nombre} x {i} {nombre* i}\n"
        f .write(ligne)

# 2.Affichage
print ( "Table générée dans 'table.txt' ." )
