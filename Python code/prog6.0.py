matrix_bord = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

for rij in matrix_bord:
    for lamp in rij:
     if lamp == 0:
      print(" ", end="")
    else:
     print("o", end="")
print()
