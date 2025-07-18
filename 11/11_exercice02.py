# Ce programme demande une liste de nombres à l’utilisateur et retourne la somme, la moyenne et le maximum.

# 1.Définition de la foncion
def stats (liste):
    somme = sum(liste)
    moyenne = somme/ len (liste)
    maximum = max(liste)
    return somme, moyenne, maximum

# 2.Entrées
nombres= [float (x) for x in input ("Entrez des nombres : ").split()]
s, m, mx = stats(nombres)

# 3.Affichage
print (f"somme : {s}")
print (f"Moyenne {m: .2f}")
print (f"Maximum: {mx} ")
