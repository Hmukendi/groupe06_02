# Ce programme demande la température et donne un conseil pour rester en bonne santé

# 1.Entrées
temp = float(input("Température (°C) : " ))

# 2.Conditions
if temp >= 35:
    print("Très chaud, restez hydraté.")
elif temp >= 25:
    print("Chaud, faites attention au soleil.")
elif temp >= 15:
    print("Température agréable.")
else:
    print("Il fait frais, couvrez-vous.")