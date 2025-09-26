# lst = []

# def getal_check(getal):
#     if getal % 2 == 0:
#         return "even"
#     else:
#         return "oneven"

# # 3 getallen vragen
# for i in range(1, 4):
#     user_input = int(input(f"Voer getal {i}: "))
#     lst.append(user_input)

# # Elk getal checken
# for getal in lst:
#     even_of_oneven = getal_check(getal)

#     if getal > 10:
#         groter = "groter dan 10"
#     else:
#         groter = "niet groter dan 10"

#     print(f"Getal: {getal} → {even_of_oneven}, {groter}")

lst = []


def even_of_oneven(getal):
    if (getal % 2 == 0):
        return "even"
    else:
        return "oneven"


for i in range(1, 4):
    user_input = int(input(f"voer het getal {i}:"))
    lst.append(user_input)


for nummers in lst:
    if nummers > 10:
        tekst = "groter dan 10"
    else:
        tekst = "niet groter dan 10"

    print("Getal", nummers, "is", even_of_oneven(nummers), tekst)

