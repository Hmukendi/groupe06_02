# Ce programme demande plusieurs noms d’utilisateurs à l’utilisateur , Les enregistre dans un fichier, un par ligne.

# 1.Entrées
utilisateurs = []

while True :
    nom= input ( "Entrez un nom d'utilisateur (ou 'stop' pour finir) ")
    if nom.lower() == "stop" :
        break
    utilisateurs.append(nom)
    
with open ("utilisateurs.txt" , "w" , encoding="utf-8" ) as f:
    for u in utilisateurs:
        f.write(u + "\n" )

# 2.Affichage
print ( "utilisateurs enregistrés dans 'utilisateurs.txt'." )
