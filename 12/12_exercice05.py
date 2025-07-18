# Ce programme demande une phraseà l’utilisateur, calcule nombre de mots, nombre de caractères, et sauvegarde un petit rapport.

# 1.Entrées
texte = input ( "Entrez une phrase : ")

nb_mots = len (texte.split())
nb_caracteres = len (texte)

with open ( "rapport.txt" , "w" , encoding="utf-8" ) as f:
    f.write( "=== Rapport d'analyse ===\n" )
    f.write( f"Phrase : {texte}\n")
    f.write( f"Nombre de mots : {nb_mots}\n")
    f.write( f"Nombre de caractères : {nb_caracteres}\n")

# 2.Affichage
print( "Rapport sauvegardé dans 'rapport.txt'. ")
