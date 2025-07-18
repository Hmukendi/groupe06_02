# Ce programme demande un numéro de téléphone et remplace tous les chiffres sauf les 3 derniers par des *.

# 1.Entrées
numero = input("Entrez un numéro :")

# 2.Affichage
if len(numero) > 3:
    masque = "*" * (len(numero) - 3) + numero[-3:]
    print(f"Numéro masqué : {masque}")
else:
    print("Numéro trop court pour masquer.")
