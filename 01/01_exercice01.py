# Ce programme demande le prénom, l’âge, la ville et le métier d’un utilisateur, puis affiche un mini profil structuré avec une approximation du nombre de jours vécus.

# 1.Demande d'informations à L'utilisateur
prenom = input ("Entrez votre prénom : ")
age = int (input ( "Entrez votre âge : "))
ville = input ("Entrez votre ville : ")
metier = input ("Entrez votre métier : ")

# 2.Approximation des jours vécus
jours_vecus = age* 365

# 3.Affichage formaté
print ("\n=== PROFIL UTILISATEUR ===" )
print (f"Prénom: {prenom}")
print (f"Âge : {age} ans ({jours_vecus} jours vécus environ)")
print (f"Ville : {ville}")
print (f"Métier: {metier}")