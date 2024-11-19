import string
import random
import secrets

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

password_length = int(input("Enter password length (minimum 8)\n"))
allow_uppercase = input("Would you like to add uppercase? y/n\n").lower()
allow_num = input("Would you like to add number? y/n\n").lower()
allow_symbols = input("would you like symbols? y/n \n").lower()

password2 = ""
if password_length >= 8:
    if allow_uppercase == "y" and allow_num =="y" and allow_symbols == "y" :
        for add in range(0,password_length):
            password2 += secrets.choice(lowercase_letters + uppercase_letters + symbols + numbers)
    elif allow_uppercase == "n" and allow_num =="y" and allow_symbols == "y" :
        for add in range(0, password_length):
            password2 += secrets.choice(lowercase_letters + symbols + numbers)
    elif allow_uppercase == "y" and allow_num =="n" and allow_symbols == "y" :
        for add in range(0, password_length):
            password2 += secrets.choice(lowercase_letters + uppercase_letters + symbols)
    elif allow_uppercase == "y" and allow_num =="y" and allow_symbols == "n" :
        for add in range(0, password_length):
            password2 += secrets.choice(lowercase_letters + uppercase_letters + numbers)
    else:
        print("at least 2 of the option needs to be yes")

    print(password2)
else:
    print("password length must be more than 8")
