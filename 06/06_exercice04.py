# Ce programme demande un mot de passe à l’utilisateur et continue à redemander tant qu’il n’est pas correct.

# Entrées et Affichage
mdp = ""
while mdp != "Python2025":
    mdp = input ("Entrez le mot de passe :")
    if mdp != "Python2025":
        print("Mot de passe incorrect, réessayez.")
print("Mot de passe correct, accès autorisé.")