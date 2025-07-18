# Ce programme demande un mot à l’utilisateur et vérifie si ce mot est un palindrome

# 1.Définition de la foncion
def est_palindrome (mot):
    return mot== mot[::-1]

# 2.Entrées
mot= input ("Entrez un mot : ")

# 3.Affichage
if est_palindrome(mot):
    print ("c'est un palindrome." )
else :
    print ("ce n'est pas un palindrome." )
