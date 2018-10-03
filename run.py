def welcome():
    return "Welcome to Epic Rater \n"

def signup_sign_menu():
    output = "Select an option"
    output += "\n 1. Signup"
    output += "\n 2. Sigin"
    return output

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