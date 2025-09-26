def standaardprijs(afstand_km):
    if afstand_km < 0:
        return 0
    elif afstand_km > 50:
        return 15 + (0.60 * afstand_km)
    else:
        return 0.80 * afstand_km


def ritprijs(leeftijd, is_weekend, afstand_km):
    prijs = standaardprijs(afstand_km)

    if leeftijd < 12 or leeftijd >= 65:
        korting = 0.65 if is_weekend else 0.70
    elif is_weekend:
        korting = 0.60
    else:
        korting = 1.00

    return prijs * korting


# 🧾 Invoer
afstand_km = float(input("Aantal gereden KM: "))
leeftijd = int(input("Wat is uw leeftijd? "))
weekend_input = input("Rijdt u in het weekend? (ja/nee): ").strip().lower()

is_weekend = weekend_input == "ja"

# 💰 Berekening en uitvoer
prijs = ritprijs(leeftijd, is_weekend, afstand_km)
print(f"Totale ritprijs: €{round(prijs, 2)}")
