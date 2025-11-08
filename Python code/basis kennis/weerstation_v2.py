def analyseer_weer_v2(temperaturen, regen):
    
    droogste_dagen = []
    natste_dagen = []
    
    min_neerslag = min(regen)
    max_neerslag = max(regen)
    
    gemiddelde_temp = sum(temperaturen)/ len(temperaturen)
    gemiddelde_neerslag = sum(regen) / len(regen)
    
    for dag, (temps, neerslag) in enumerate(zip(temperaturen, regen), start = 1):
        if neerslag == min_neerslag:
            droogste_dagen.append((dag, temps, neerslag))
        if neerslag == max_neerslag: 
            natste_dagen.append((dag, temps, neerslag))
            
    return gemiddelde_temp, gemiddelde_neerslag, droogste_dagen, natste_dagen


def analyseer_meerdere_weken(data):    
    resultaat_per_week = []
    for i, week in enumerate(data, start = 1):
        temp = week[0]
        rain = week[1]
        week_resultaat = analyseer_weer_v2(temp, rain)
        resultaat_per_week.append((i, week_resultaat))
        
    return resultaat_per_week
    
temperaturen = [14, 17, 19, 10, 21, 10, 16]
regen = [2, 0, 1, 0, 3, 5, 0]

data = [
    ([14, 17, 19, 10, 21, 10, 16], [2, 0, 1, 0, 3, 5, 0]),
    ([15, 16, 18, 9, 22, 11, 17], [1, 0, 0, 0, 4, 2, 0])
]
weken_resultaat = analyseer_meerdere_weken(data)

for i, binnenste_resultaat in weken_resultaat:
    print(f"Week {i}: Gem. temp {binnenste_resultaat[0]:.1f}, Gem. regen {binnenste_resultaat[1]:.1f}")



















# resultaat = analyseer_weer_v2(temperaturen, regen)
# print(analyseer_meerdere_weken(data))
# print(f"Gemiddelde temperatuur is:{resultaat[0]}")
# print(f"Gemiddelde neerslag is {resultaat[1]}")
# print(f"Droogste dag/en waren: {', '.join(f'Dag {dag[0]}: {dag[1]}c, {dag[2]}mm ' for dag in resultaat[2])}") 
# print(f"De natste dag/en waren: {', '.join(f'Dag: {dag[0]}: {dag[1]}c, {dag[2]}mm' for dag in resultaat[3])}")