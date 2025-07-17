# Ce programme lit une distance (en km) et un temps (en heures) et calcule la vitesse moyenne (km/h) et la vitesse en m/s.

# 1.Données
distance_km = float(input ("Distance (km) : "))
temps_h = float(input("Temps (heures) : "))

# 2.Vitesse
vitesse_kmh = distance_km / temps_h
vitesse_ms = (distance_km * 1000) / (temps_h * 3600)

# 3.Affichage
print(f"Vitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"Vitesse moyenne : {vitesse_ms:.2f} m/s")