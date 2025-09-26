temp = []
for i in range(1,8):
    user_input = int(input("Voer een nummer van de temperatuur"))
    temp.append(user_input)
    gemiddelde = (sum(temp) / len(temp))
    
print(round(gemiddelde,2))

