# Ce programme demande l’ancienneté (années) et la performance (note 1 à 5) et calcule les avanatages d'un employé

# 1.Entrées
anciennete = int(input("Années d'ancienneté : "))
note = int(input("Note de performance (1-5) : "))

# 2.Conditions
if anciennete >= 5:
    if note >= 4:
        prime = 2000
    else:
        prime = 1000
else:
    if note >= 4:
        prime = 500
    else:
        prime = 0
print(f"Prime attribuée {prime} $.")
