def temp_functie(temperaturen):
    lst = []
    for temps in temperaturen.split(","):
        lst.append(int(temps))

    min_getal = min(lst)
    max_getal = max(lst)
    aantal_getalen = len(lst)
    gemiddelde = sum(lst) / aantal_getalen
    
    teller = 0
    for getal in lst:
        if getal > gemiddelde:
            teller += 1
    
    lst.sort()
    return lst, min_getal, max_getal, aantal_getalen, gemiddelde, teller


resultaat = temp_functie("22,18,20,25,21,19,23")
for i in resultaat:
    print(i)
