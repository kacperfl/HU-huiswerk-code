temperaturen = [20, 22, 18, 21]
regen = [0, 5, 2, 3]

for dag, (temp, rain) in enumerate(zip(temperaturen, regen), start = 1):
    print(f"Dag: {dag} temperatuur: {temp} regen hoeveelheid in mm: {rain}")