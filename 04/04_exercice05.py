# Ce programme demande le type de plat (viande, poisson, végétarien) et simule une commande de resaurant

# 1.Entrées
plat = input("choisissez un plat (viande/poisson/végétarien) : ").lower()

# 2.Conditions
if plat == "viande":
    cuisson = input("cuisson (saignant/à point/bien cuit) : ").lower()
    print(f"Vous avez choisi une viande {cuisson} .")
elif plat == "poisson":
    sauce = input("Sauce (citron/beurre) : ").lower()
    print(f"Vous avez choisi un poisson sauce {sauce} .")
elif plat == "végétarien":
    choix = input("souhaitez-vous une salade ou des pâtes? : ").lower()
    print (f"Vous avez choisi: {choix} .")
else:
    print("choix invalide.")
