# Ce programme demande trois notes (sur 20), calcule la moyenne et dit si l’étudiant est reçu (moyenne ≥ 10) ou non.

# 1.entrées
note1 = float(input("Première note : "))
note2 = float(input("Deuxième note : "))
note3 = float(input("Troisième note : "))

# 2.Calcul de la moyenne
moyenne = (note1 + note2 + note3) / 3
print(f"Moyenne {moyenne:.2f}")

# 3.Condition
if moyenne>= 10:
    print("L'étudiant est reçu.")
else :
    print("L'étudiant n'est pas reçu." )