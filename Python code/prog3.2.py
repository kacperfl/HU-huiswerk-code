leeftijd = int(input("Wat is jou leeftijd?"))
nederlaands_passport = input("Heb jij een nederlaands passport?")

if (leeftijd >= 18 and nederlaands_passport.lower() == "ja"):
    print("Gefeliceerd je mag stemmen!")
else:
    print("Sorry je mag nog niet gaan stemmen")