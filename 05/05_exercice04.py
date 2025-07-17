# Ce programme crée une liste de carrés pour les nombres de 1 à 20, puis affiche uniquement ceux supérieurs à 100.

# 1.Entrées
carres = []

# 2.Conditions
for i in range ( 1 , 21):
    carres.append(i ** 2 )
print("Tous les carrés :", carres)

print("carrés > 100 :")
for val in carres:
    if val > 100:
        print(val)
