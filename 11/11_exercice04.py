# Ce programme convertit un montant en dollars vers euros, francs CFA et livres sterling.

# 1.Définition de la foncion
def convertir(usd):
    eur = usd * 0.93
    cfa = usd * 610
    gbp = usd * 0.79
    return eur, cfa, gbp

# 2.Entrées
montant= float (input ( "Montant en USD "))
eur, cfa, gbp = convertir(montant)

# 3.Affichage
print(f" {montant} USD {eur: .2f} EUR, {cfa: .2f} CFA, {gbp: .2f} GBP")
