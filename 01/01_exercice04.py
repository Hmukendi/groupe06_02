# Ce programme affiche une note sur 100, qui est donnée au depart sur 20.

note_20 = float(input("Note sur 20 : "))
note_100 = (note_20 / 20) * 100
print(f"Note sur 100: {note_100:.1f}")