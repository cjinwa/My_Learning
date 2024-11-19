uppercase_checker = 0
symbol_checker = 0
number_checker = 0

password = input("enter password\n")

password_list = list(password)

for check in password_list:
    if check.isnumeric():
        number_checker +=1
    if not check.isnumeric() and not check.isupper() and not check.islower():
        symbol_checker +=1
    if check.isupper():
        uppercase_checker += 1

print(uppercase_checker,symbol_checker,number_checker)

if len(password) >= 8 :
    if symbol_checker >= 4 or number_checker >=4 or uppercase_checker >= 4 :
        print("your password strength is very strong")
    elif symbol_checker >= 3 or number_checker >=3 or uppercase_checker >= 3 :
        print("your password strength is strong")
    elif symbol_checker >= 2 or number_checker >= 2 or uppercase_checker >= 2:
        print("your password strength is valid but medium")
    elif symbol_checker < 2 or number_checker < 2 or uppercase_checker < 2:
        print("your password strength is valid but weak")

else:
    print("your password has less than 8 characters making it weak")