# Ce programme demande un nombre à l’utilisateur et affiche sa table de multiplication de 1 à 12 sous forme formatée.

# 1.Entrées
nombre = int(input("Entrez un nombre pour sa table de multiplication : "))

# 2.Affichage
print(f"=== Table de {nombre} ===")
for i in range (1 , 13):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")