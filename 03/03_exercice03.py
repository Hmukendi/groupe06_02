# Ce programme demande la valeur d'un panier, fixe les frais pour la livraison et affiche le prix total à payer

# 1.Entrées
panier = float(input("Montant du panier ($) : "))

# 2.Conditions
if panier >= 100:
    frais = 0
elif panier >= 50:
    frais = 5
else:
    frais = 10

# 3.Affichage
total= panier + frais
print(f"Frais de livraison : {frais} $")
print(f"Total à payer : {total:.2f} $")