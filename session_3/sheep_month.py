menu = [5, 7, 300 , 90, 24, 50 ,75]

print("Hello , my name is Phuc and there are my sheep sizes :")
print( *menu , sep=", ")

month = 0
loop = True

while loop :
    month += 1
    print("Month" , month)
    print("One Month has passed , now here is my flock")
    i=-1
    menu[0] = menu[0] + 50
    for i in range (len(menu)-1):
        i += 1

        menu[i] = menu[i] +50
        
    print(*menu,sep=", ")
    biggest = max(menu)

    print("Now my biggest sheep has size",biggest, "let's shear it ")
    n = (menu.index(biggest))
    menu[n] = 8
    print("After shearing, here is my flock ")
    print(*menu,sep=", ")
    
    if month == 3:
        loop = False
        print("My flock has size in total :", sum(menu))
        total= sum(menu) * 2
        print("I Would get", sum(menu), "*","2$  = ",total)