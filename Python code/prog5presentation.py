lange_zin = "Barbara had een bar, waar ze rabarbar verkocht, en die daarom de rabarbarbarbarabar werd genoemd."
lange_zin = lange_zin.replace("rabarbar", "rabarber")
print(lange_zin)


lange_string = "Niemand verwacht de Spaanse Inquisitie!# In feite, zij die de Spaanse Inquisitie wel verwachten..." 
speciaal_teken = lange_string.find("#")
print(lange_string[0: speciaal_teken])
