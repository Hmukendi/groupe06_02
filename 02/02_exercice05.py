# Ce programme est un convertisseur de devises qui convertit un montant en dollars vers euros,francs CFA, et livres sterling.
# Taux : 1 USD → 0,93 EUR, 1 USD → 610 CFA, 1 USD → 0,79 GBP.

# 1.Entrées
usd = float(input("Montant en USD : "))

# 2.Conversion
eur = usd * 0.93
cfa = usd * 610
gbp = usd * 0.79

# 3.Affichage
print(f"{usd} USD = {eur:.2f} EUR")
print(f"{usd} USD = {cfa:.2f} CFA")
print(f"{usd} USD = {gbp:.2f} GBP")