# Ce programme demande un mot de passe et vérifie sa validité

# 1.Entrées
mdp = input("Entrez un mot de passe : ")

# 2.Conditions
if len(mdp) >= 8 and any(c.isdigit() for c in mdp) and any (c.isupper() for c in mdp):
    print("Mot de passe valide.")
else :
    print ("Mot de passe invalide." )