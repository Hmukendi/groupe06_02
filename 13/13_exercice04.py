# Ce programme demande un entier positif et reste une boucle tant que la saisie est invalide.

# 1.Entrées
while True:
    try :
        n = int (input ( "Entrez un entier positif "))
        if n < 0:
            raise ValueError( "Nombre négatif interdit." )
        break
    except ValueError as e:
        print (f"Erreur : {e}")

# 2.Affichage
print(f"Vous avez saisi : {n}")
