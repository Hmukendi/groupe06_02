# Ce programme demande une adresse email et vérifie si elle se termine par "@gmail.com" puis affiche un message de validation.

# 1.Entrées
email = input("Entrez votre email ")

# 2.Verification et Affichage
if email.endswith("@gmail.com"):
    print("Email valide (Gmail).")
else:
    print("Email invalide ou non Gmail.")
