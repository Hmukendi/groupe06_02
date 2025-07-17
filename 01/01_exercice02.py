# Ce programme crée une mini "fiche produit" qui contient : nom, prix, stock, remise et calculle le prix final aprés remise.

# 1.Définition des variables
nom_produit = "Cahier "
prix = 200
stock = 100
remise = 0.15 # 15%

# 2.calcul du prix final
prix_final = prix * (1 - remise)

# 3.Affichage
print (f"Produit : {nom_produit}")
print (f"Prix initial : {prix} $")
print (f"Remise: {remise* 100}%")
print (f"Prix final : {prix_final: .2f} $")
print (f"Stock disponible: {stock}")