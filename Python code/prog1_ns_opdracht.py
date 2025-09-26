# Gemaakt door Kacper Flak :D
def standaardprijs(afstandKM):
    ticket_prijs = (0.80 * afstandKM)
    if (afstandKM < 0):
        ticket_prijs = 0
    elif (afstandKM > 50):
        ticket_prijs = 15 + (0.60 * afstandKM)
    return ticket_prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    normaal_prijs = standaardprijs(afstandKM)
    if (weekendrit == False and (leeftijd < 12 or leeftijd >= 65)):
        normaal_prijs = normaal_prijs * 0.70
    elif (weekendrit == True and (leeftijd < 12 or leeftijd >= 65)):
        normaal_prijs = normaal_prijs * 0.65
    elif (weekendrit == True and (leeftijd >= 12 and leeftijd < 65)):
        normaal_prijs = normaal_prijs * 0.60
    return normaal_prijs


km_input = float(input("Aantal gereden KM:"))
age_input = int(input("Wat is uw leeftijd?"))
weekend_input = input("Rijd u in het weekend? (ja/nee): ")

weekendrit = True if weekend_input.lower() == "ja" else False

calc_ritprijs = ritprijs(age_input, weekendrit, km_input)
print(round(calc_ritprijs, 2))
