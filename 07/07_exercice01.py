# Ce programme demande une liste de nombres à l’utilisateur et la trie

# 1.Entrées
entree = input("Entrez des nombres séparés par des espaces :")

# 2.Tri
liste = [int(x) for x in entree.split()]
n = len(liste)
for i in range(n):
    for j in range(0, n - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

# 3.Affichage
print(f"Liste triée : {liste}")
