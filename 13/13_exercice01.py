# Ce programme demande deux nombres à l’utilisateur et affiche leur quotient.

# Entrées et Affichage
try :
    a = float ( input ("Nombre 1: "))
    b = float ( input ( "Nombre 2 :"))
    result = a / b
except ZeroDivisionError:
    print ( "Erreur : Division par zéro !" )
else :
    print (f"Résultat : {result}")
