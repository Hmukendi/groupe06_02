# Ce programme demande un nombre entier positif à l’utilisateur et calcule sa factorielle

# 1.Entrées
n = int(input("Entrez un entier positif :"))
while n < 0 :
    print("veuillez entrer un nombre positif.")
    n = int(input("Entrez un entier positif: "))

# 3.Calcul
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

# 3.Affichage
print(f"Factorielle de {n} = {fact} ")