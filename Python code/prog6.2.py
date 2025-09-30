studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ] 

def gemiddelde_per_student(studentencijfers): 
    antw = []
    for student in studentencijfers:
        gemiddelde = sum(student) / len(student)
        antw.append(gemiddelde)
    return antw
    
   
def gemiddelde_van_alle_studenten(studentencijfers):
    gem_per_student = gemiddelde_per_student(studentencijfers)
    antw = sum(gem_per_student) / len(gem_per_student)
    return antw

print(gemiddelde_per_student(studentencijfers)) 

print(gemiddelde_van_alle_studenten(studentencijfers))