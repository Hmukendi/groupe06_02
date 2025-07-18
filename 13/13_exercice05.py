# Ce programme demande un nombre à l’utilisateur et calcule  sa racine carrée.

import math

# Entrées et Affichage
try :
    x = float (input ("Entrez un nombre : ") )
    if x < 0:
        raise ValueError( "Nombre négatif, pas de racine réelle." )
    racine= math.sqrt(x)
except ValueError as e:
    print (f"Erreur : {e}")
else :
    print (f"Racine carrée :{racine}")
finally :
    print ("Fin du calcul." )
