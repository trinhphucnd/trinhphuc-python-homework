count = 0 
menu = ["T-shirt", "Sweater"]
while True :
  
    n = str(input("Welcome to our shop, what do you want (C, R, U, D)?"))
    
    if n == "R":
        print("Our items: ", *menu, sep=", ")

    elif n == "C":
        nitems = input("New items ? ")
        menu.append(nitems)
        print("Our items: ", *menu, sep=", ")

    elif n == "U":
        upos = int(input('Update position? '))
        nitem = input('New item? ')
        menu[upos-1] = str(nitem)
        print("Our items: ", *menu, sep=", ")
    
    elif n == "D":
        dpos = int(input("Del possition ? "))
        del menu[dpos]
        print("Our items :", *menu, sep=", ")
    else:
        print("No support")
  
  