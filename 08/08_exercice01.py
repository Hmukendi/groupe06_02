# Ce programme demande une liste de dictionnaires représentant des livres (titre, auteur, année) et affiche tous les livres publiés après 2010.

# 1.Entrées
livres = [
    {"titre": "Python débutant", "auteur": "Dupont", "année": 2008},
    {"titre": "Maîtriser Python", "auteur": "Durand", "année": 2015},
    {"titre": "Python avancé", "auteur": "Martin", "année": 2021}
]

# 2.Affichage
print("Livres publiés après 2010 :")
for livre in livres:
    if livre["année"] > 2010:
        print(f"{livre['titre']} ({livre['année']}) - {livre['auteur']}")
