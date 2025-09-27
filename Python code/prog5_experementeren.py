with open('oefening_5_2_kaartnummers.txt', 'r') as f:
    nummers = []
    namen = []
    for regel in f:
        regel = regel.strip()
        nummer_waarde = regel.split(',')[0]
        naam_waarde = regel.split(',')[1]

        nummers.append(nummer_waarde)
        namen.append(naam_waarde)
        
    for nummers, naam in zip(nummers, namen):
        if int(nummers) > 500000:
            print(nummers, naam)
            
    # print(nummers)
    # print(namen)
