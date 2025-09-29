def random_functie():
    with open("oefening_5_2_kaartnummers.txt", "r") as f:
        nummers_lst = []
        naam_lst = []
        for regels in f:
            regels = regels.strip()
            nummer, naam = regels.split(',')
            nummer = int(nummer.strip())
            naam = naam.strip()
            nummers_lst.append(nummer)
            naam_lst.append(naam)
            
        max_num = max(nummers_lst)
        index = nummers_lst.index(max_num)
        max_naam = naam_lst[index]
    return max_num, max_naam


print(random_functie())
