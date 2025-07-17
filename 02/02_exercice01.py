# Ce programme demande deux nombres à l’utilisateur et affiche : Leur somme, Leur différence,Leur produit,Leur quotient (division réelle),Leur division entière ,Leur reste (modulo)

# 1.Entrée
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# 2.Calculs
somme = a + b
difference = a - b
produit = a * b
quotient= a / b if b != 0 else "Division par zéro"
division_entiere = a // b if b != 0 else "Division par zéro"
reste = a % b if b != 0 else "Division par zéro"

# 3.Affichage des résultats
print ( f"sornme : {somme}")
print (f"Différence : {difference}")
print (f"Produit : {produit}")
print (f"Quotient : {quotient}")
print (f"Division entière : {division_entiere}")
print (f"Reste : {reste}")