import re

def password_check():
    p = input("enter the password: ")
    
    if len(p) < 8:
        print("At least 8 characters")
        return password_check()
    else:
        if not re.search(r"[A-Z]", p):
            print("Invalid_Password!Should have atleast one uppercase")
            return password_check()
        if not re.search(r"[a-z]", p):
            print("Invalid_Password! Should have atleast one lowercase")
            return password_check()
        if not re.search(r"\d", p):
            print("Invalid_Password! Should have atleast one digit")
            return password_check()
        if re.search(r"\s", p):
            print("Invalid_Password! Should not contain void spaces")
            return password_check()
        if not re.search(r"[!@#$%^&*(),.?';{}<>|_/+-]", p):
            print("Invalid_Password! Should have atleast one special symbol")
            return password_check()
    strength_check(p)


def strength_check(p):
    if len(p) <=9: 
        print("Weak Password")
    elif len(p) <= 11:
        print("Medium Password")
    elif len(p) <= 12:
        print("Strong Password")
    elif len(p) >= 15:
        print("Very Strong Password")

password_check()
