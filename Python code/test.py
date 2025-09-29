
# num = int(input("Geef een nummer: "))
# totaal = 0

# while num != 0:
#  totaal += num
#  num = int(input("Geef een nummer: "))
# print( "Totaal is", totaal )

# zonder while loop:

# for i in range(1, 10):
#     pos_getal = int(input("Voer een positief getal: "))
#     if pos_getal <= 0:
#         print("U mag geen negatief getal invoeren")
#         continue
#     else:
#         print("Uw positief getal is: " + str(pos_getal))
#         break


teller = 0
user_input = 0

while teller < 5:
    user_input = int(input("Voer een positief getal: "))
    user_input += 0
    if user_input < 0:
        print("U mag geen negatief getal invoeren")
        continue
    else:
     print("Uw positief getal is: " + str(user_input))
     break
        
