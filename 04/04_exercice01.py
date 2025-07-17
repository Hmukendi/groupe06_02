# Ce programme demande l’âge et la situation (étudiant, salarié, retraité) puis détermine le tarif pour un abonnement cinéma:


# 1.Entrées
age = int(input("Âge : "))
statut = input("Statut (étudiant/salarié/retraité) : ").lower()

# 2.Conditions
if age < 18:
    tarif = 5
else:
    if 18 <= age <= 25:
        if statut == "étudiant":
            tarif = 6
        elif statut == "salarié":
            tarif = 8
        else:
            tarif = 10  # cas inattendu
    else:
        if statut == "retraité":
            tarif = 7
        else:
            tarif = 10

# 3.Affichage
print(f"Votre tarif est de {tarif} $.")
