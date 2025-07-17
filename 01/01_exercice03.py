# Ce script convertit une durée en secondes (entrée sous forme d'heures, minutes,secondes).

# 1.Entrée utilisateur
heures= int (input ("Nombre d'heures : "))
minutes = int (input ("Nombre de minutes : "))
secondes= int (input ("Nombre de secondes : "))

# 2.Conversion
total_secondes = heures * 3600 + minutes * 60 + secondes

# 3.Résultat
print (f"Durée totale = {total_secondes} secondes.")