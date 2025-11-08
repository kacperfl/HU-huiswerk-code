def analyseer_weer(data_temp, data_regen):
    boven_gemiddelde_temps = []
    droge_warme_dagen = []
    gemiddelde_temp = sum(data_temp) / len(data_temp)
    gemiddelde_neerslag = sum(data_regen) / len(data_regen)
    weer = zip(data_temp, data_regen)
      
    for temp in data_temp:
        if temp > gemiddelde_temp:
            boven_gemiddelde_temps.append(temp)
      
    for value in weer:
        if value[1] > 0 and value[0] > 18:
            droge_warme_dagen.append(value)
            
    return gemiddelde_temp, gemiddelde_neerslag, boven_gemiddelde_temps, droge_warme_dagen
        
temperaturen = [14, 17, 19, 10, 21, 10, 16]
regen = [2, 0, 1, 0, 3, 5, 0]

resultaat = analyseer_weer(temperaturen, regen)
print(f"De gemiddelde neerslag was: {resultaat[1]:.2f} en gemiddelde temp was: {resultaat[0]:.2f}")
print(f"De boven gemiddelde termpartauren zijn: {', '.join(str(dag) for dag in resultaat[2])}")
print(f"De dagen waar regen viel maar ook boven 18 graden was: {', '.join(str(dag) for dag in resultaat[3])}")