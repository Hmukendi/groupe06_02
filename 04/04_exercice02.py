# Ce programme demande le rôle (employé, visiteur, sécurité) verifie si il faut ,le badge et gère l'accés à un batiment

# 1.Entrées
role = input("Rôle (employé/visiteur/sécurité) : ").lower()

# 2.Conditions
if role == "employé":
    badge = input("Badge valide ? ( oui/non) : ").lower()
    if badge == "oui":
        print("Accès autorisé.")
    else:
        print("Accès refusé, badge invalide.")
elif role == "visiteur":
    rdv = input("Avez-vous un rendez-vous? (oui/non) : ").lower()
    if rdv == "oui":
        print("Accès autorisé.")
    else:
        print("Accès refusé, pas de rendez-vous.")
elif role == "sécurité":
    print("Accès autorisé.")
else:
    print("Accès refusé, rôle inconnu.")