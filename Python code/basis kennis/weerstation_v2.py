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
    
    
temperaturen = [14, 17, 19, 10, 21, 10, 16]
regen = [2, 0, 1, 0, 3, 5, 0]
resultaat = analyseer_weer_v2(temperaturen, regen)

print(f"Gemiddelde temperatuur is:{resultaat[0]}")
print(f"Gemiddelde neerslag is {resultaat[1]}")
print(f"Droogste dag/en waren: {', '.join(f"Dag {dag[0]}: {dag[1]}c, {dag[2]}mm" for dag in resultaat[2])}")