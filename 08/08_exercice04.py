# Ce programme demande une phrase à l’utilisateur et affiche le nombre de mots ayant plus de 5 lettres

# 1.Entrées
phrase = input("Entrez une phrase :")
mots = phrase.split()
count = 0

# 2.comptage
for mot in mots:
    if len(mot) > 5:
        count += 1

# 3.Affichage
print(f"Nombre de mots > 5 lettres {count}")
