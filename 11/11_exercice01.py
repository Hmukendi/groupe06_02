# Ce programme demande 2 nombres et une opération  à l’utilisateur et retourne le résultats de cette opération.

# 1.Définition de la foncion
def calculer (a, b, op):
    if op== "+" :
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op== "/":
        if b != 0 :
            return a/ b
        else :
            return "Division par zéro impossible."
    else :
        return "Opérateur non valide."

# 2.Entrées
x = float (input ( "Nombre: " ))
y = float (input ( "Nombre 2: "))

# 2.Calcul
operation = input ("Opération (+, -, *, /) : ")
resultat = calculer(x, y, operation)

# 3.Affichage
print (f"Résultat : {resultat}")
