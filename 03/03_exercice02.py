# Ce programme demande une note sur 100 et attribue une mention

# 1.Entrées
note = float(input("Entrez votre note sur 100 : "))

# 2.Conditions
if note >= 90:
    print("Mention : Excellent")
elif note >= 75:
    print("Mention : Très bien")
elif note >= 60:
    print("Mention : Bien")
elif note >= 50:
    print("Mention : Passable")
else:
    print("Mention : Insuffisant")
