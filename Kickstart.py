
    leng = input()
    password = input()
    lower = False
    upper = False
    digit = False
    special = False
    length = False

    for i in password:
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
        if i.isdigit():
            digit = True
        if i in "!@#$%^&*()-+":
            special = True
        if len(password) >= 7:
            length = True

    while length == False:
        if upper == False:
            password += "A"
            upper = True
        if lower == False:
            password += "a"
            lower = True
        if digit == False:
            password += "1"
            digit = True
        if special == False:
            password += "!"
            special = True
        else:
            password += "!"
        if len(password) >= 7:
            length = True


    if upper == False:
        password += "A"
    if lower == False:
        password += "a"
    if digit == False:
        password += "1"
    if special == False:
        password += "!"
    
    y = password
    print(x)
    print("Case #{}: {}".format(x, y))
    