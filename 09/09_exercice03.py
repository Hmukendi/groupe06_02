# Ce programme demande un texte et un mot à chercher. Compte combien de fois ce mot apparaît.

# 1.Entrées
texte = input("Entrez un texte : ").lower()
mot = input("Mot à chercher : ").lower()

# 2.Comptage
compte = texte.count(mot)

# 3.Affichage
print(f"Le mot '{mot}' apparaît {compte} fois.")
