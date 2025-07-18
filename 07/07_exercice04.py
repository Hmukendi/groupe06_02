# Ce programme crée une liste de tuples contenant le nom d’un étudiant et sa note et affiche tous les étudiants ayant une note supérieure ou égale à 15.

# 1.Entrées
etudiants = [("Alice", 16), ("Paul", 14), ("Sara", 18), ("John", 12)]

# 2.Affichage
print("Étudiants avec note >= 15 :")
for nom, note in etudiants:
    if note >= 15:
        print(f"{nom} - {note}")
