maand_nummer = int(input("Wat is de maand nummer (1/12)?"))

if maand_nummer == 12 or 1 <= maand_nummer <= 2:
    print("Winter")
elif 3 <= maand_nummer <= 5:
    print("Lente")
elif 6 <= maand_nummer <= 8:
    print("Zomer")
elif 9 <= maand_nummer <= 11:
    print("Herfst")
else:
    print("U heeft een verkeerde waarde ingevoerd")