# Ce programme demande un texteà l’utilisateur et tente de le convertir en entier

# 1.Entrées
valeur = input ("Entrez un entier : ")

# 2.Affichage
try :
    entier= int (valeur)
except ValueError:
    print ("Erreur : Ce n'est pas un entier valide." )
else :
    print (f"Vous avez entré l'entier :{entier}")
