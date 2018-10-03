from utilities import *
def enter_option():
    option = int(input("Your option \n"))
    if option == 1:
        return "You have selected Sign up"
    else:
        if option == 2:
            return "You have selected Signin"
        else:
            return "Invalid Input"

print(welcome())
print(signup_sign_menu())
print(enter_option())