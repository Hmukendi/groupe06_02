# Ce programme demande un nom de fichier à l’utilisateur et tente de l’ouvrir.

# 1.Entrées
nom_fichier = input ("Nom du fichier à lire :")

# 2.Affichage
try :
    with open (nom_fichier, "r" , encoding="utf-8" ) as f:
        contenu= f.read()
except FileNotFoundError:
    print ("Erreur: Fichier introuvable." )
else :
    print ("contenu du fichier:" )
    print (contenu)
