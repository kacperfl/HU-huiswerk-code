teller = 0

while True:
    user_input = int(input("Voer een getal uit: "))
    teller += 1
    
    if user_input == 0:
        print(f"Er zijn {teller} getallen ingevoerd, de som is: {sum(user_input)}")
    break