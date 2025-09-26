def new_password(oldpassword, newpassword):
    if newpassword == oldpassword and len(newpassword) <= 6:
        return False
    elif newpassword != oldpassword and len(newpassword) > 6:
     return True
    else:
     return False

user_oldpassword = input("Wat is uw oud wachtwoord?")
user_newpasssword = input("Wat is uw nieuw wachtwoord?")

print(new_password(user_oldpassword, user_newpasssword))

