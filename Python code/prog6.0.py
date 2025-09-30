def gemiddelde_per_student(studentencijfers):
    antw = []

    for student in studentencijfers:
        antw.append(sum(student) / len(student))

    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    gem_per_student = gemiddelde_per_student(studentencijfers)
    antw = sum(gem_per_student) / len(gem_per_student)
    return antw

studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
resultaat1 = gemiddelde_per_student(studentencijfers)
print(resultaat1)
resultaat2 = gemiddelde_van_alle_studenten(studentencijfers)
print(resultaat2)