def pretty_functie():
    with open("oefening_5_2_kaartnummers.txt", 'r') as f:
        resultaat = ""
        for regel in f:
            kaart_info = regel.split(",")
            resultaat += kaart_info[1].strip()+  " heeft kaartnummer: "+  kaart_info[0].strip() + "\n"
        return resultaat

print(pretty_functie())
            