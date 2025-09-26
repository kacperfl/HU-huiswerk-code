def lang_genoeg(len_gebruiker_cm):
    if len_gebruiker_cm >= 120:
        return "Gefeliceerd je mag op de achtbaan!"
    else:
        return "Sorry je bent niet lang genoeg :("

user_input = int(input("Wat is jou lengte?"))
print(lang_genoeg(user_input))