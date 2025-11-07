# 1.  ik maak eerst ee functie aan die als parameter de lijst krijgt met de temperarturen
# 2. ik moet daarna de gemiddelde uitrekenen door de totaal gedeeldoor aantal items, totaal met sum(), lengte met len()
# 3. Index vinden doe ik door de ingebouwde functie index te gebruiken en aangeven dat ik de kleinste waarden wil
# daarnaast zet ik bij de varbalen de daadwerkelijk waarde dat bij de index hoort, ik doe ook + 1 omdat maandag == dag 1 niet 0
# 4. ik return meerde waardens het is dus een tulpe ik moet dan in de print statment spcifiek geven welke waardens ik precies nodig heb en welke
# info ik wil tonen op de plek, alles wordt netjes in variabelen gezet zodat het duiudelijk is over welke element het gaat
# In kort: functie krijgt een parameter ik bereken de gemiddelde met standaard formule in de print wordt het afgerond met :.2f maar kan ook met round()
# daarna bereken in de kleinste en hoogste waarden en zijn indexes, dat doe ik met index functie maar kan ook enumerate in loop gebruiken en zo berkenen
# ik doe bij indexes + 1 omdat ik het bij de bijbehoorde dag moet doen en dag 0 bestaat niet, ik return alles in de tulpe, de lijst is tempartaturen van temps dus aanroep zet ik variabelen als operoepn van de functie
# f-string om netjes de bijbehoorden waardens te returnen
def temps(lst):
    gemiddelde = sum(lst) / len(lst)
    kleinste_waardes_index = []
    min_value = min(lst)
    for i, num in enumerate(lst):
        if num == min_value:
            kleinste_waardes_index.append(i + 1)
            
    return min_value, kleinste_waardes_index, gemiddelde

temperaturen = [14, 17, 19, 10, 21, 10, 16, 10]
aanroep = temps(temperaturen)

print(f"Gemiddelde temperatuur: {aanroep[2]:.2f}")
#   list comprehension was niet mijn idee: geholpen door ai
print(f"laagste temperatuur: {aanroep[0]} op dag(en) {', '.join(str(dag) for dag in aanroep[1])}")
