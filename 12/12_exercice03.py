# Ce programme demande une activité à l’utilisateur et l’ajoute dans un fichier journal.

# 1.Entrées
activite = input ("Décrivez votre activité du jour : ")

with open ("journal.txt" , "a" , encoding="utf-8" ) as f:
    f.write(activite + "\n" )

# 2.Affichage
print ( "Activité ajoutée dans 'journal.txt'." )
