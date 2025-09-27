def gemiddelde(input):
    word_split = input.split()
    teller = 0
    for i in word_split:
        teller += len(word_split)
    gemiddelde_waarde = teller / len(i)
    return gemiddelde_waarde


userinput = input("Voer een random zin in:")
print(gemiddelde(userinput))
