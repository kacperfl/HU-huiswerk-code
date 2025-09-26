grondgetallen = [1, -5, 12, 5, -2, 4, -1]

def kwadraten_som(grondgetallen):
    new_getalen = []  
    for pos_getalen in grondgetallen:
        if pos_getalen > 0:
            new_getalen.append(pos_getalen ** 2)
    return sum(new_getalen)

print(kwadraten_som(grondgetallen))  
