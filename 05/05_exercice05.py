# Ce programme demande une liste de mots à l’utilisateur (saisie séparée par des espaces),compte le nombre total de voyelles dans tous les mots.

# 1.Entrées
mots = input("Entrez des mots séparés par des espaces :").split()
voyelles = "aeiouyAEIOUY"
total_voyelles = 0

# 2.Conditions
for mot in mots:
    for lettre in mot:
        if lettre in voyelles:
            total_voyelles += 1

# 3.Affichage
print(f"Nombre total de voyelles : {total_voyelles}")
