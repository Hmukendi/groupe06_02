# Ce programme demande une liste de notes à l’utilisateur, calcule la moyenne et sauvegarde le résultat dans un fichier.

# 1.Entrées
notes = [float(x) for x in input ("Entrez des notes : ").split() ]
moyenne= sum(notes) / len(notes)

with open ("statistiques.txt" , "w" , encoding="utf-8" ) as f:
    f.write( f"Notes : {notes}\n")
    f.write( f"Moyenne : {moyenne: .2f}\n")

# 2.Affichage
print( "statistiques sauvegardées dans ·'statistiques.txt'. ")
