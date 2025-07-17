# Ce programme est un petit "calculateur de factures" qui demande à l’utilisateur un montant HT et un taux de TVA, calcule et affiche le montant TTC.

# 1.Entrée
montant_ht = float(input ("Montant HT ($) : "))
taux_tva = float (input ("Taux de TVA(%) : "))

# 2.conversion en coefficient multiplicateur
taux_coef = taux_tva / 100

# 3.Calcul TTC
montant_ttc = montant_ht * (1 + taux_coef)

# 4.Affichage
print (f"Montant TTC {montant_ttc:.2f} $")