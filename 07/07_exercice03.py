# Ce programme demande une liste de nombres à l’utilisateur et affiche le Maximum, le Minimum et la Moyenne.

# 1.Entrées
entree = input("Entrez des nombres : ")
liste = [float(x) for x in entree.split()]

# 2.Conditions
maximum = max(liste)
minimum = min(liste)
moyenne = sum(liste) / len(liste)

# 3.Affichage
print(f"Max : {maximum}")
print(f"Min : {minimum}")
print(f"Moyenne : {moyenne:.2f}")
